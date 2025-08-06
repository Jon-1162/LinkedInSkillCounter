import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import time


df = pd.read_csv('linkedinjobs.csv')
skillSetReference = {'Rust', 'PowerShell', 'Linode', 'Akamai', 'OpenGL', 'WordPress', 'Keras', 'ASP.NET CORE', 'Webpack', 'Lua', 'Unreal Engine', 'Asana', '.NET', 'Eclipse', 'Oracle Cloud Infrastructure (OCI)', 'ZMK', 'Fastify', 'Pandas', 'Code::Blocks', 'Jira', 'PHP', 'Elm', 'GDScript', 'Cobol', 'OpenShift', 'Electron', 'doctest', 'OpenCL', 'cppunit', 'Visual Studio Code', 'Nix', 'Basecamp', 'Go', 'CodeIgniter', 'Bun', 'Kotlin', 'Drupal', 'Gradle', 'Netbeans', 'MariaDB', 'Solr', 'Astro', 'Strapi', 'WebStorm', 'Capacitor', 'Oracle', 'Fortran', 'Geany', 'Xcode', 'Python', 'Catch2', 'InfluxDB', 'Hadoop', 'Couch DB', 'Microsoft Lists', 'MSBuild', 'Yii 2', 'Erlang', 'Nim', 'Visual Basic (.Net)', 'Firebase', 'MATLAB', 'Boost.Test', 'Azure Devops', 'VSCodium', 'PyCharm', 'CLion', 'PostgreSQL', 'Puppet', 'Nano', 'Next.js', 'MongoDB', 'Spacemacs', 'Neo4J', 'Swift', 'Visual Studio Solution', 'AngularJS', 'Firebird', 'Stack Overflow for Teams', 'Linear', ' C ', 'mlflow', 'Vue.js', 'VBA', 'Scala', 'Flutter', 'PythonAnywhere', 'Cargo', 'Chocolatey', 'Node.js', 'Podman', 'Fly.io', 'build2', 'PhpStorm', 'Dagger', 'Clickup', 'Julia', 'SwiftUI', 'Neovim', 'Elasticsearch', 'Composer', 'C++', 'Scikit-Learn', 'pnpm', 'Supabase', 'MySQL', 'Flask', 'Elixir', 'EventStoreDB', 'C#', 'Amazon Web Services (AWS)', 'JavaScript', 'Google Test', 'Homebrew', 'Terraform', 'Torch/PyTorch', 'Vim', 'Lucid', 'Zephyr', 'Spring Boot', 'NestJS', "LLVM's Clang", 'ASP.NET', 'RubyMine', '.NET MAUI', 'Couchbase', 'HTML/CSS', 'Presto', 'Solid.js', 'Spring Framework', 'TensorFlow', 'Android Studio', 'Goland', 'Doxygen', 'Qt Creator', 'Spyder', 'GNU GCC', 'Ruby', 'Micronaut', 'GTK', 'RabbitMQ', 'Rider', 'Notepad++', 'Prolog', 'Opencv', 'Deno', 'Rad Studio (Delphi, C++ Builder)', 'Assembly', 'Svelte', 'GitHub Discussions', 'Shortcut', 'Delphi', 'Vultr', 'React Native', 'Solidity', 'Cosmos DB', 'React', 'SCons', 'JAX', 'Unity 3D', 'Jupyter Notebook/JupyterLab','Snowflake', 'Tauri', 'Godot', 'Cloudflare', 'Symfony', 'Arduino', 'Helix', 'Crystal', 'F#', 'SQLite', 'DataGrip', 'BBEdit', 'MFC', 'RavenDB', 'Digital Ocean', 'npm', 'Apex', 'Confluence', 'Render', '.NET Framework (1.0 - 4.8)', 'jQuery', 'Pacman', 'H2', 'Phoenix', 'Ruby on Rails', 'Ada', 'CUDA', 'Yarn', 'Vercel', ' R ', 'Java', 'Blazor', 'Xamarin', 'Sublime Text', 'OpenStack', 'Groovy', 'Colocation', 'Miro', 'Gatsby', 'Clickhouse', 'Obsidian', 'Cordova', 'Meson', 'Chef', 'NuGet', 'Nuxt.js', 'SQL', 'Tidyverse', 'IBM Cloud Or Watson', 'YouTrack', 'Google Cloud', 'Alibaba Cloud', 'Cassandra', 'QMake', 'Qt', 'Microsoft SQL Server', 'Dart', 'NumPy', 'Bash/Shell (all shells)', 'Play Framework', 'Redis', 'Htmx', 'RStudio', 'Markdown File', 'Roslyn', 'Haskell', 'Ninja', 'Airtable', 'Ktor', 'Hetzner', 'Laravel', 'Pip', 'Heroku', 'Express', 'deleteMeLater', 'Datomic', 'FastAPI', 'Docker', 'PlatformIO', 'Ansible', 'Remix', 'Angular', 'IBM DB2', 'CMake', 'Dynamodb', 'Kate', 'Lisp', 'Zig', 'Monday.com', 'CUTE', 'Pulumi', 'Trello', 'OVH', 'Apache Kafka', 'Emacs', 'Cloud Firestore', 'TypeScript', 'Microsoft Access', 'DuckDB', 'DirectX', 'Quarkus', 'IntelliJ IDEA', 'Notion', 'Perl', 'Clojure', 'Rasberry Pi', 'Managed Hosting', 'Databricks', 'Apache Spark', 'Hugging Face Transformers', 'Vite', 'Databricks SQL', 'APT', 'Ionic', 'VMware', 'OCaml', 'Ant', 'Kubernetes', 'Visual Studio', 'MicroPython', 'Scaleway', 'MSVC', 'Microsoft Planner', 'Make', 'IPython', 'Cockroachdb', 'Wikis', 'TiDB', 'Django', 'Redmine', 'Smartsheet', 'Firebase Realtime Database', 'BigQuery', 'Maven (build tool)', 'Ruff', 'Microsoft Azure', 'Fleet', 'Netlify', 'Objective-C'}

# 1. In how many jobs a string for a skill occurrences. This is just counting skills even if they are mentioned once to get a aggregate of skill count 
# make a dictionary of skills that adds 1 to the value whener it occours for thye 1st time and loop through all job ids
def getSkillCounts():
    setCountDict = dict.fromkeys(skillSetReference, 0)

    for row in df.itertuples():
        for skill in skillSetReference:
            if skill in row.jobDesc:
                setCountDict[skill] = setCountDict[skill] + 1 

    returnDF = pd.DataFrame([setCountDict])
    returnDF.to_csv('skillSetOccurrence.csv', index=True)
    return returnDF


# 2. In jobs where the string occurrences what was its frequency compared to other technical skills. This is a count and compare. This is to help determine relative importance of skills within a job
#  just count the number or times a skill occours for each job. With the end goal of just counting string instance of a skill and summing for a 1D stat at the end
def getSkillAllInstancesSumCount():
    sumCountDict = dict.fromkeys(skillSetReference, 0)

    for row in df.itertuples():
        jobDescList = row.jobDesc.split()
        for word in jobDescList:
            for skill in skillSetReference:
                if skill in word:
                    sumCountDict[skill] = sumCountDict[skill] + 1 
    returnDF = pd.DataFrame([sumCountDict])
    returnDF.to_csv("allSkillInstancesCount.csv", index=True)
    return returnDF
    
# # 3. Correlation of a string with other string. So where a string occurrences how likely was it to be in the job description with another skill
# # This will agregate over 
# 2 make 2d matrix like the below example to get frequency scan each job and add to occurrences
# # jobid    py    java      c
# # 1        10     2        0
# # 2        5      5       11
# # 3        0      0        3

# # Given one skill is present how many time does another skill string occur
# #             java | py | rust | c
# # java       |x      15          14     
# # py         | 7     x           11           
# # rust       |
# # c          | 15      6     
def coOccurance():
    # Makes list of column titles
    jobIDwSkillsDfColumns = ["jobId"]
    for skill in skillSetReference:
        jobIDwSkillsDfColumns.append(skill)

    # Makes a df from the list of column  titles
    jobIDwSkillsDf = pd.DataFrame(columns=jobIDwSkillsDfColumns)

    # Loops through job data to make a df like the following example table
    # jobid    py    java      c
    # 1        10     2        0
    # 2        5      5       11
    # 3        0      0        3
    for row in df.itertuples():
        setCountDictRowTemplate = dict.fromkeys(skillSetReference, 0)
        setCountDictRowTemplate["jobID"] = 0
        setCountDictNewRow = setCountDictRowTemplate
        print("fresh rewrite Dict ")
        print(setCountDictNewRow)
        
        setCountDictNewRow["jobId"] = row[1]    
        for skill in skillSetReference:
            if skill in row.jobDesc:
                setCountDictNewRow[skill] =  1 
            # Add row dictionary to main df
        jobIDwSkillsDf.loc[len(jobIDwSkillsDf)] = setCountDictNewRow



    # # Given one skill is present, how many times does another skill co-occur in the same job description
    # # Output format (example):
    # #             Java | Python | Rust | C
    # # Java       |  x     15       14     2
    # # Python     |  7      x        11     1
    # # Rust       |  4      6         x     0
    # # C          | 15      6         3     x

    # Initialize the co-occurrence matrix
    skillsList = sorted(skillSetReference)
    coOccurrenceDf = pd.DataFrame(0, index=skillsList, columns=skillsList)

    # Fill co-occurrence matrix
    for index, row in jobIDwSkillsDf.iterrows():
        # Extract list of skills present in the job description
        present_skills = [skill for skill in skillsList if row[skill] == 1]
        
        # For each pair of skills, increment co-occurrence count
        for i in range(len(present_skills)):
            for j in range(len(present_skills)):
                if i != j:
                    skill_i = present_skills[i]
                    skill_j = present_skills[j]
                    coOccurrenceDf.at[skill_i, skill_j] += 1

    # Optional: remove self-cooccurrence (diagonal), or just leave it at 0
    print("Skill Co-occurrence Matrix")
    print(coOccurrenceDf)

    coOccurrenceDf.to_csv('coOccurrenceDf.csv', index=True)