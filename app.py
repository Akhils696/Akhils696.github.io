'''from flask import Flask, render_template, Response
import cv2
import gps

app = Flask(__name__)

# Initialize camera (drone camera)
camera = cv2.VideoCapture(0)

# Function to generate frames from the camera
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Yield the frame to the webpage
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for video feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for GPS data
@app.route('/gps_data')
def gps_data():
    session = gps.gps()  # Start GPS session
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    report = session.next()
    if report['class'] == 'TPV':
        lat = report['lat']
        lon = report['lon']
    return f"Latitude: {lat}, Longitude: {lon}"

# Route for thermal sensor data (Assume AMG8833)
@app.route('/thermal_data')
def thermal_data():
    # Add code to fetch data from your thermal sensor
    thermal_reading = "Thermal data goes here"
    return thermal_reading

# Route for rescue radar data
@app.route('/radar_data')
def radar_data():
    # Add code to fetch data from your rescue radar
    radar_reading = "Radar data goes here"
    return radar_reading

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
