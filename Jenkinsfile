@Library('my-shared-library') _

pipeline{

    agent any

    parameters{

        choice(name: 'action', choices: 'create\ndelete', description: 'Choose create/Destroy')
        string(name: 'ImageName', description: "name of the docker build", defaultValue: 'javapp')
        string(name: 'ImageTag', description: "tag of the docker build", defaultValue: 'v1')
        string(name: 'DockerHubUser', description: "name of the Application", defaultValue: 'taisserysuhaib')
    }

    stages{
         
        stage('Git Checkout'){
                    when { expression {  params.action == 'create' } }
            steps{
            gitCheckout(
                branch: "main",
                url: "https://github.com/praveen1994dec/Java_app_3.0.git"
            )
            }
        }
         stage('Unit Test maven'){
         
         when { expression {  params.action == 'create' } }

            steps{
               script{
                   
                   mvnTest()
               }
            }
        }
         stage('Integration Test maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnIntegrationTest()
               }
            }
        }
       //  stage('Static code analysis: Sonarqube'){
       //   when { expression {  params.action == 'create' } }
       //      steps{
       //         script{
                   
       //             def SonarQubecredentialsId = 'sonarqube-api'
       //             statiCodeAnalysis(SonarQubecredentialsId)
       //         }
       //      }
       // }
       // stage('Quality Gate Status Check : Sonarqube'){
       //   when { expression {  params.action == 'create' } }
       //      steps{
       //         script{
                   
       //             def SonarQubecredentialsId = 'sonarqube-api'
       //             QualityGateStatus(SonarQubecredentialsId)
       //         }
       //      }
       // }
        stage('Maven Build : maven'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   mvnBuild()
               }
            }
        }     
        stage('Push to JFrog') {
            when { expression { params.action == 'create' } }
            steps {
                script {
                    def artifactoryUrl = "http://54.91.52.166:8082/artifactory/example-repo-local/"  // Replace with your Artifactory URL and repository name
                    def username = "admin"  // Replace with your Artifactory username
                    def password = "1234@Qwer"  // Replace with your Artifactory password or API key
                    def artifactPath = "/var/lib/jenkins/workspace/java-jfrog-assign-2/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"  // Replace with the path to your artifact

                    def curlCommand = """
                        curl -u ${username}:${password} -X PUT ${artifactoryUrl}/${artifactPath} -T ${artifactPath}
                    """
            
                    sh curlCommand
                }
            }
        }        
        stage('Docker Image Build'){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerBuild("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
         stage('Docker Image Scan: trivy '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageScan("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }
        stage('Docker Image Push : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImagePush("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }   
        stage('Docker Image Cleanup : DockerHub '){
         when { expression {  params.action == 'create' } }
            steps{
               script{
                   
                   dockerImageCleanup("${params.ImageName}","${params.ImageTag}","${params.DockerHubUser}")
               }
            }
        }      
    }
}
