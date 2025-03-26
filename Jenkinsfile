pipeline {
    agent any

    environment {
        IMAGE_NAME = "ubuntu_flask"
        CONTAINER_NAME = "contenedor_uf"
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/Aler011/jenkins_docker_webframework.git'
            }
        }

        stage('Construir imagen docker') {
            steps {
                script {
                    def buildTag = env.BUILD_ID
                    bat "docker build -t %IMAGE_NAME%:%BUILD_ID% ."
                }
            }
        }

        stage('Detener contenedor existente') {
            steps {
                script {
                    bat """
                        docker ps -q --filter "name=%CONTAINER_NAME%" | findstr . >nul && docker stop %CONTAINER_NAME% || exit 0
                    """
                }
            }
        }

        stage('Ejecutar nuevo contenedor') {
            steps {
                script {
                    bat "docker run -d --name %CONTAINER_NAME% -p 5001:5000 %IMAGE_NAME%:%BUILD_ID%"
                }
            }
        }
    }
}
