from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from youtube import youtube_playlist_to_mp3, create_zip_from_folder

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json().get('url')
    if not data:
        return jsonify({"error": "Missing 'url' in request"}), 400

    """
    The body should be of form
    {
        'url': string
    }
    """
    title = youtube_playlist_to_mp3(data)
    data = create_zip_from_folder(f"playlists/{title}")
    return send_file(data, 
                     as_attachment=True, 
                     download_name=f"{title}.zip",
                     mimetype="application/zip")

if __name__ == '__main__':
    app.run(debug=True)