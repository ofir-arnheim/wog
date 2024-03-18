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
                    def result = bat(script: 'python tests/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error 'Selenium test failed'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                expression {
                    currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'wog-docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'wog-docker-credentials') {
                            bat 'docker tag wog:latest ofirarnheim/wog:latest'
                            bat 'docker push ofirarnheim/wog:latest'
                        }
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                bat 'docker stop wog'
                bat 'docker rm wog'
            }
        }
    }
}
