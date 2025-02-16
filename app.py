import os
import uuid
from flask import Flask, render_template, request, jsonify, url_for
from rembg import remove

app = Flask(__name__)
# Define the folder for storing processed images
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'processed')

# Create the processed folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    # List processed PNG images for the file history
    processed_files = os.listdir(app.config['UPLOAD_FOLDER'])
    processed_files = [f for f in processed_files if f.lower().endswith('.png')]
    return render_template('index.html', processed_files=processed_files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    try:
        # Read the uploaded image data and process it with rembg
        input_data = file.read()
        output_data = remove(input_data)
        
        # Generate a unique filename for the processed image
        filename = f"{uuid.uuid4().hex}.png"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'wb') as out_file:
            out_file.write(output_data)
        
        # Generate a URL to the processed image file
        file_url = url_for('static', filename=f'processed/{filename}')
        return jsonify({'status': 'success', 'filename': filename, 'url': file_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Listen on host 0.0.0.0 and port 2000
    app.run(debug=True, host='0.0.0.0', port=2000)