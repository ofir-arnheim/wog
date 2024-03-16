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
                    docker.build('.')
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    docker.run('-p 8777:20000 --name wog wog-latest')
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
                dockerContainer().stop()
                dockerContainer().remove()
            }
        }
    }
}
