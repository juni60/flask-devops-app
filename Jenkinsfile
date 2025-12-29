pipeline {
    agent {
        label 'Jenkins-Agent'
    }

    environment {
        APP_NAME = "flask-devops-app"
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out source code"
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo "Setting up Python environment"
                sh '''
                    python3 --version
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies"
                sh '''
                    . ${VENV}/bin/activate
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "requirements.txt not found"
                    fi
                '''
            }
        }

        stage('Run Application Test') {
            steps {
                echo "Running Flask app test"
                sh '''
                    . ${VENV}/bin/activate
                    python -c "import flask; print('Flask import successful')"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker image"
                sh '''
                    docker build -t ${APP_NAME}:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to Docker Hub"
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag ${APP_NAME}:latest $DOCKER_USER/${APP_NAME}:latest
                        docker push $DOCKER_USER/${APP_NAME}:latest
                    '''
                }
            }
        }

    }

    post {
        success {
            echo "Pipeline SUCCESS: Image built & pushed to Docker Hub"
        }
        failure {
            echo "Pipeline FAILED"
        }
        always {
            echo "Cleanup completed"
        }
    }
}


