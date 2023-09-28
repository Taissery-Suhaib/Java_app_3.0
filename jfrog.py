import requests

# Replace these with your Artifactory repository details
artifactory_url = "http://34.227.98.230:8082/artifactory/example-repo-local/"
username = "admin"
password = "1234@Qwer"  # Alternatively, use an access token or API key

# Path to the JAR file you want to upload
jar_file_path = "/var/lib/jenkins/workspace/java-assign-2/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"

# Create a session with authentication
session = requests.Session()
session.auth = (username, password)

# Define the URL for uploading
upload_url = f"{artifactory_url}/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"  # Remove jar_file_path from here

try:
    with open(jar_file_path, 'rb') as jar_file:
        # Perform the PUT request to upload the JAR file
        response = session.put(upload_url, data=jar_file)

        # Check the response for success or error
        if response.status_code == 201:
            print("JAR file uploaded successfully to Artifactory.")
        else:
            print(f"Failed to upload JAR file. Response code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
