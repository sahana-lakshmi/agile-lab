STEP 1: Develop the Application
Actions
1. Read the question and identify the required features and versions.
2. Create the project folder and open it in VS Code.
3. Implement the application and its required features.
4. Write tests for the application.
5. Install dependencies and verify the application.
Files to create
- app.py : Application
- test_app.py : Tests
- requirements.txt : Dependencies
- Dockerfile : Docker configuration
- Jenkinsfile : Jenkins pipeline
Commands to run (in the project folder):
python -m pip install -r requirements.txt
python -m pytest -v
python -m flake8 app.py test_app.py --count --statistics
python app.py

Check the application at http://localhost:5000, if it uses port 5000. Stop it with Ctrl+C.
STEP 2: GitHub Version Control
Actions
1. Create a GitHub repository.
2. Initialise Git in the project folder.
3. Commit and push the application.
4. Create the required version branches.
5. Implement the correct features in each branch.
6. Commit and push each version.
Commands to run

Initial push:
git init
git add .
git commit -m "Initial application implementation"
git branch -M version-v1
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin version-v1

Create and push additional branches:
git switch -c version-v2
git push -u origin version-v2

git switch version-v1
git switch -c version-v3
git push -u origin version-v3

After making changes to a branch:
git add .
git commit -m "Update application features"
git push

Replace: YOUR_GITHUB_REPOSITORY_URL with the repository URL. If Git is already initialised or the branches already exist, don't recreate them.
STEP 3: Jenkins CI/CD Pipeline
Actions
1. Start Jenkins and open http://localhost:8081.
2. Create a new Pipeline job.
3. Configure Pipeline script from SCM → Git.
4. Enter the GitHub repository URL.
5. Select the branch containing Jenkinsfile.
6. Set Script Path to Jenkinsfile.
7. Create and configure the Jenkinsfile.
8. Add Docker Hub credentials in Jenkins with ID dockerhub-creds.
9. Save and run the pipeline.
File to create
- Jenkinsfile
Commands to start Jenkins (if using the WAR file):
java -jar jenkins.war --httpPort=8081

Pipeline stages, in order
1. Checkout code
2. Install dependencies
3. Run tests
4. Check code quality
5. Build Docker image
6. Push image to Docker Hub
7. Deploy to Kubernetes
Remember: Configure the correct repository, branch names, image name, filenames, and ports in the Jenkinsfile.
STEP 4: Testing and Code Quality
Actions
1. Run the tests locally.
2. Check code quality.
3. Run the Jenkins pipeline.
4. Open the Jenkins build's Console Output.
5. Fix any failed stages and rerun the pipeline.
Commands
python -m pytest -v
python -m flake8 app.py test_app.py --count --statistics

Evidence to save
- Successful pytest results.
- Flake8 output showing 0 errors.
- Successful Jenkins build and stage results.
If the application or test filenames differ, update the Flake8 command accordingly.
STEP 5: Docker Image Build
Actions
1. Create the Dockerfile.
2. Check that it copies the correct application files.
3. Confirm the application's listening port.
4. Build the Docker image.
5. Verify that the image exists.
6. Optionally run the container locally to test it.
File to create
- Dockerfile
Commands

Build the image:
docker build -t YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v1 .

List images:
docker images

Run a local test container:
docker run -d --name myapp-test -p 5000:5000 YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v1

Check the container:
docker ps

Stop and remove the test container when finished:
docker stop myapp-test
docker rm myapp-test

Evidence to save: A screenshot of the successful Docker image build.
STEP 6: Push Images to Docker Hub
Actions
1. Sign in to Docker Hub.
2. Create a repository.
3. Configure Docker Hub credentials in Jenkins.
4. Run the Jenkins pipeline for each required version.
5. Check that every image is pushed successfully.
6. Open the repository's Tags tab and verify the tags.
Commands for manual pushing

Log in:
docker login -u YOUR_DOCKERHUB_USERNAME

Push each required version:
docker push YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v1
docker push YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v2
docker push YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v3

Evidence to save
- Screenshot of the real Docker Hub repository showing all required tags.
Important: Build each version's correct image before pushing it. If Jenkins handles the push, use Jenkins instead of repeating the manual commands.
STEP 7: Kubernetes Deployment
Actions
1. Start Docker Desktop.
2. Ensure Kubernetes is running.
3. Check the Kubernetes context.
4. Deploy the required application versions.
5. Expose each deployment through a service.
6. Check deployments, pods, and services.
7. Open the application using the assigned NodePort.
Commands

Check the current context:
kubectl config current-context

Select Docker Desktop if required:
kubectl config use-context docker-desktop

Check cluster nodes:
kubectl get nodes

Manual deployment (only if Jenkins has not already deployed it)
Deploy v1:
kubectl create deployment library-v1 --image=YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE_NAME:v1

Expose v1:
kubectl expose deployment library-v1 --type=NodePort --port=5000 --target-port=5000

Repeat for v2 and v3, changing the deployment names and image tags.

If Jenkins already deployed the application, do not create duplicate deployments or services.
Verify deployment
Run all three commands:
kubectl get deployments
kubectl get pods
kubectl get services

If a pod fails, inspect it:
kubectl describe pod POD_NAME
kubectl logs POD_NAME

Replace POD_NAME with the actual pod name.

Open the application using the NodePort shown by kubectl get services, for example:
http://localhost:30473

Use your actual assigned port, not necessarily 30473.
