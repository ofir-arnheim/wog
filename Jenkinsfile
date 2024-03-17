pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t wog .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker run -d -p 8777:20000 --name wog wog'
                }
            }
        }

        stage('Run Selenium Test') {
            steps {
                script {
                    def result = bat(script: 'python tests/e2e.py http://localhost:8777', returnStatus: true)
                    if (result != 0) {
                    error 'Selenium test failed'
                }
            }
        }

        post {
            always {
            // Stop and remove the container after execution
                script {
                    bat 'docker stop wog'
                    bat 'docker rm wog'
                }
            }
        }
    }
}
