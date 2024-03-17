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
                    sh 'docker build -t wog .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker stop wog'
                    sh 'docker rm wog'
                    sh 'docker run -d -p 8777:20000 --name wog'
                }
            }
        }

        stage('Run Selenium Test') {
            steps {
                script {
                    sh 'python tests/e2e.py http://localhost:8777'
                }
            }
        }
    }
}
