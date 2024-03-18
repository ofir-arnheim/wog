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
                    sh 'docker run -d -p 8777:20000 --name wog wog'
                }
            }
        }

        stage('Run Selenium Test') {
            steps {
                script {
                    def result = sh(script: 'python tests/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error 'Selenium test failed'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'wog-docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'wog-docker-credentials') {
                            sh 'docker tag wog:latest ofirarnheim/wog:latest'
                            sh 'docker push ofirarnheim/wog:latest'
                        }
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                sh 'docker stop wog'
                sh 'docker rm wog'
            }
        }
    }
}
