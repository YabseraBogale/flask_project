class JobTitle():
    def __init__(self) -> None:
        self.title=['New Grad Software Engineer', 'CNC Programmer', 'Puppet Engineer', 'Artificial Intelligence (AI) / Machine Learning Engineer', 
                'DEVOPS MANAGER', 'Search Engine Optimization', 'PyTest Engineer', 'AWS DevOps Engineer', 'New Relic Engineer', 'Data Engineer', 
                'OpenStack Engineer', 'JavaScript Developer', 'Salesforce Developer', 'Senior SRE Architect', 'Programmer', 'Groovy Engineer', 
                'Junior Developer', 'GAME DEVELOPER', 'Software Developer', 'kubernetes Administrator', 'Artificial Intelligence Researcher', 
                'Data Analyst', 'Chef Operations Engineer', 'Build and Release Engineer', 'Tech Sales Engineer', 'QA Engineer', 'PHP Developer', 
                'Datadog Engineer', 'AGILE PROJECT MANAGER', 'Senior Build and Release Engineer', 'DATA MODELER', 'FULL-STACK DEVELOPER', 'Jira Administrator', 
                'Chef InSpec Engineer', 'Splunk Engineer', 'Bamboo Engineer', 'Junior Front End Developer', 'Cloud architect', 
                'Senior Software Developer', 'Mobile Application Developer', 'GCP DevOps Engineer', 'PYTHON DEVELOPER', 'Full Stack Developer', 
                'Senior DevOps Engineer', 'Ansible Automation Engineer', 'Unity Developer', 'Senior Software Engineer', 'Database manager', 
                'SRE Engineer', 'TECHNICAL ACCOUNT MANAGER', 'Embedded Software Engineer', 'Selenium Engineer', 'Machine learning Architect', 
                'Big Data Engineer', 'Senior .NET Developer', 'Oracle Developer', 'Twistkock Engineer', 'Micro services / API Lead Designer', 
                'Entry Level Programmer', 'Web Developer', 'Junior IOS Developer', 'AWS Solutions Architect', 'ELK Engineer', 'Oracle SQL Developer', 
                'Senior DevOps Architect', 'ML Engineer', 'QA (QUALITY ASSURANCE) SPECIALIST', 'MAVEN Engineer', 'CLOUD ARCHITECT', 
                'Network and Systems Administrator', 'Packer Engineer', 'Bitbucket Engineer', 'Data Scientist', 'FluentD Engineer', 'Git Engineer',
                'Senior Ansible Development Engineer', 'COMPUTER GRAPHICS ANIMATOR', 'Artificial Intelligence', 'Puppet Operations Engineer', 
                'Entry Level Software Developer', 'FRONT-END DEVELOPER', 'Web Designer (UI/UX Designer)', 'Vault Engineer', 'SYSTEMS ADMINISTRATOR', 
                'TECHNICAL LEAD', 'Computer Systems Analyst', 'SRE Architect', 'DATA ANALYST', 'DevOps Architect', 'Senior Site reliability Engineer', 
                'Jenkins Engineer', 'Production Support Engineer', 'Splunk Enterprise Security Engineer', 'Python Developer', 'Gradle Engineer', 
                'JIRA Engineer', 'Robotics Engineer', 'XL Deploy Engineer', 'Artificial intelligence / Machine Learning Engineer', 'Mulesoft Developer', 
                'Nexus Engineer', 'Blockchain Developer', 'GitLab Engineer', 'OpenShift Engineer', 'IT Manager', 'UDeploy Engineer', 'JUnit Engineer', 
                'React Developer', 'Artificial Intelligence / Machine Learning Leader', 'Falco Engineer', 'Junior Software Engineer', 
                'Senior DevSecOps Architect', 'WordPress Developer', 'WORDPRESS DEVELOPER', 'UI DESIGNER', 'Gerrit Administrator', 
                'Principle Engineer in Machine Learning', 'DATABASE ADMINISTRATOR', 'Artifactory Engineer', 'BUSINESS SYSTEMS ANALYST', 
                'Computer Research Scientist', 'Grafana Engineer', 'DevSecOps Architect', 'Java Developer', 'Cloud Security Engineer', 
                'Senior Data Analysts', 'Data Architect', 'Principle Engineer in Artificial Intelligence', 'IOS Developer', 'SOFTWARE DEVELOPERS', 
                'Big Data Architect', 'JaCoCO Engineer', 'SQL Developer', 'Junior Software Developer', 'Nomad Engineer', 'Data Analysts', 
                'MOBILE APP DEVELOPER', 'Confluence Engineer', 'SonarQube Engineer', 'Artificial intelligence Architect', 
                'Kubernetes Operations Engineer', 'C# Developer', 'Principle Engineer in Big Data', 'Operations Engineer', 
                'Senior Front End Developer', 'AppDynamics Engineer', 'TeamCity Engineer', 'Senior IOS Developer', 'Admin Big Data', 
                'Front End Web Developer', 'Cloud engineer', 'Senior Build Engineer', 'Istio Engineer', 
                'Full Stack Python Developer/Programmer/Engineer','Full Stack Python Engineer','Full Stack Python Programmer', 'Entry Level Software Engineer', 'Senior Developer', 'Nagios Engineer', 
                'RUBY ON RAILS DEVELOPER', 'Cloud administrator', 'UX DESIGNER', 'Artifactory Administrator', 'Sharepoint Developer', 
                'Cloud automation engineer', 'Computer Programmer', 'MOBILE DEVELOPER', 'Ansible Operations Engineer', 'Developer', 
                'Machine Learning Engineer', 'computer science', 'Azure DevOps Engineer', 'TFS Engineer', 'Information Security Analyst', 
                'Senior SRE Engineer', 'Senior DevSecOps Engineer', 'UI Developer', 'Game Developer', 'Senior Web Developer', 
                'Principle Engineer in Data Analysis', 'Big Data Specialist', 'Senior Cloud Architect', 'Terraform Engineer', 'Coder', 
                'INTERACTION DESIGNER', 'Build Engineer', 'FRONT-END DESIGNER', 'SECURITY SPECIALIST', 'Junior Web Developer', 'WORDPRESS', 
                'Computer Hardware Engineer', 'DevOps Engineer', 'Consult Engineer', 'ACCESSIBILITY SPECIALIST', 'Github Engineer', 
                'Computer Network Architect', 'Zabbix Engineer', 'Entry Level Developer', 'Gerrit Engineer', 'Network Engineer', 
                'Coverage.py Engineer', 'Software Engineer', 'Entry Level Network Engineer', 'Notary Engineer', 'DevSecOps Engineer', 
                'DATA SCIENTIST', 'Cloud network engineer', 'Database Administrator', 'Powershell Engineer', 'Application Security Engineer', 
                'Kubernetes Engineer', 'FRAMEWORKS SPECIALIST', 'Front End Developer', 'PRODUCT MANAGER', 'Entry Level Web Developer', 
                'Full Stack JAVA Developer/Programmer/Engineer', 'Envoy Engineer', 'Programmer Analyst', 'DATA ARCHITECT', 'SYSTEMS ENGINEER', 
                'Android Developer', 'Fortify Engineer', 'Site Reliability Engineer (Kubernetes – Docker)', 'Director of Engineering', 'Jr Developer', 
                'INFORMATION ARCHITECT', 'Docker Engineer', 'Artificial Intelligence / Machine Learning Sr.Leader', 'Octopus Deploy Engineer', 'Prometheus Engineer']
    def GiveJobTitle(self):
        return self.title


larget=0
for i in JobTitle().GiveJobTitle():
    if(larget<=len(i)):
        largest=len(i)

print("largest:",largest)
