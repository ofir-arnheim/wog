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
                    def wogImage = docker.build('wog', '.')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.withRun('-p 8777:20000 --name wog') {
                    }
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

    post {
        always {
            script {
                dockerImage.stop()
                dockerImage.remove(force: true)
            }
        }
    }
}
