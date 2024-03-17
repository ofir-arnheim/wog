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
                    bat 'docker stop wog'
                    bat 'docker rm wog'
                    bat 'docker run -d -p 8777:20000 --name wog wog'
                }
            }
        }

        stage('Run Selenium Test') {
            steps {
                script {
                    bat 'python tests/e2e.py http://localhost:8777'
                }
            }
        }
    }
}
