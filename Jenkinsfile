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
                echo " Setting up Python environment"
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
    }

    post {
        success {
            echo " Pipeline SUCCESS for flask-devops-app"
        }
        failure {
            echo " Pipeline FAILED"
        }
        always {
            echo " Cleanup completed"
        }
    }
}
