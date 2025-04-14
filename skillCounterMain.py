import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import time

# response = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=4200885089&keywords=Software%20Engineer&origin=JOBS_HOME_KEYWORD_SUGGESTION&refresh=true")
# reponse1 = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"

# with open('job.txt', 'w', encoding='utf-8') as fp:
#     fp.write(html)


# linkedInURL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SWE&location=Las%20Vegas,%20Nevada,%20United%20States&geoId=100293800&currentJobId=3415227738&position=1&pageNum=0&start=25"
skillSet = {'Rust', 'PowerShell', 'Linode', 'Akamai', 'OpenGL', 'WordPress', 'Keras', 'ASP.NET CORE', 'Webpack', 'Lua', 'Unreal Engine', 'Asana', '.NET', 'Eclipse', 'Oracle Cloud Infrastructure (OCI)', 'ZMK', 'Fastify', 'Pandas', 'Code::Blocks', 'Jira', 'PHP', 'Elm', 'GDScript', 'Cobol', 'OpenShift', 'Electron', 'doctest', 'OpenCL', 'cppunit', 'Visual Studio Code', 'Nix', 'Basecamp', 'Go', 'CodeIgniter', 'Bun', 'Kotlin', 'Drupal', 'Gradle', 'Netbeans', 'MariaDB', 'Solr', 'Astro', 'Strapi', 'WebStorm', 'Capacitor', 'Oracle', 'Fortran', 'Geany', 'Xcode', 'Python', 'Catch2', 'InfluxDB', 'Hadoop', 'Couch DB', 'Microsoft Lists', 'MSBuild', 'Yii 2', 'Erlang', 'Nim', 'Visual Basic (.Net)', 'Firebase', 'MATLAB', 'Boost.Test', 'Azure Devops', 'VSCodium', 'PyCharm', 'CLion', 'PostgreSQL', 'Puppet', 'Nano', 'Next.js', 'MongoDB', 'Spacemacs', 'Neo4J', 'Swift', 'Visual Studio Solution', 'AngularJS', 'Firebird', 'Stack Overflow for Teams', 'Linear', 'C', 'mlflow', 'Vue.js', 'VBA', 'Scala', 'Flutter', 'PythonAnywhere', 'Cargo', 'Chocolatey', 'Node.js', 'Podman', 'Fly.io', 'build2', 'PhpStorm', 'Dagger', 'Clickup', 'Julia', 'SwiftUI', 'Neovim', 'Elasticsearch', 'Composer', 'C++', 'Scikit-Learn', 'pnpm', 'Supabase', 'MySQL', 'Flask', 'Elixir', 'EventStoreDB', 'C#', 'Amazon Web Services (AWS)', 'JavaScript', 'Google Test', 'Homebrew', 'Terraform', 'Torch/PyTorch', 'Vim', 'Lucid', 'Zephyr', 'Spring Boot', 'NestJS', "LLVM's Clang", 'ASP.NET', 'RubyMine', '.NET MAUI', 'Couchbase', 'HTML/CSS', 'Presto', 'Solid.js', 'Spring Framework', 'TensorFlow', 'Android Studio', 'Goland', 'Doxygen', 'Qt Creator', 'Spyder', 'GNU GCC', 'Ruby', 'Micronaut', 'GTK', 'RabbitMQ', 'Rider', 'Notepad++', 'Prolog', 'Opencv', 'Deno', 'Rad Studio (Delphi, C++ Builder)', 'Assembly', 'Svelte', 'GitHub Discussions', 'Shortcut', 'Delphi', 'Vultr', 'React Native', 'Solidity', 'Cosmos DB', 'React', 'SCons', 'JAX', 'Unity 3D', 'Jupyter Notebook/JupyterLab','Snowflake', 'Tauri', 'Godot', 'Cloudflare', 'Symfony', 'Arduino', 'Helix', 'Crystal', 'F#', 'SQLite', 'DataGrip', 'BBEdit', 'MFC', 'RavenDB', 'Digital Ocean', 'npm', 'Apex', 'Confluence', 'Render', '.NET Framework (1.0 - 4.8)', 'jQuery', 'Pacman', 'H2', 'Phoenix', 'Ruby on Rails', 'Ada', 'CUDA', 'Yarn', 'Vercel', 'R', 'Java', 'Blazor', 'Xamarin', 'Sublime Text', 'OpenStack', 'Groovy', 'Colocation', 'Miro', 'Gatsby', 'Clickhouse', 'Obsidian', 'Cordova', 'Meson', 'Chef', 'NuGet', 'Nuxt.js', 'SQL', 'Tidyverse', 'IBM Cloud Or Watson', 'YouTrack', 'Google Cloud', 'Alibaba Cloud', 'Cassandra', 'QMake', 'Qt', 'Microsoft SQL Server', 'Dart', 'NumPy', 'Bash/Shell (all shells)', 'Play Framework', 'Redis', 'Htmx', 'RStudio', 'Markdown File', 'Roslyn', 'Haskell', 'Ninja', 'Airtable', 'Ktor', 'Hetzner', 'Laravel', 'Pip', 'Heroku', 'Express', 'deleteMeLater', 'Datomic', 'FastAPI', 'Docker', 'PlatformIO', 'Ansible', 'Remix', 'Angular', 'IBM DB2', 'CMake', 'Dynamodb', 'Kate', 'Lisp', 'Zig', 'Monday.com', 'CUTE', 'Pulumi', 'Trello', 'OVH', 'Apache Kafka', 'Emacs', 'Cloud Firestore', 'TypeScript', 'Microsoft Access', 'DuckDB', 'DirectX', 'Quarkus', 'IntelliJ IDEA', 'Notion', 'Perl', 'Clojure', 'Rasberry Pi', 'Managed Hosting', 'Databricks', 'Apache Spark', 'Hugging Face Transformers', 'Vite', 'Databricks SQL', 'APT', 'Ionic', 'VMware', 'OCaml', 'Ant', 'Kubernetes', 'Visual Studio', 'MicroPython', 'Scaleway', 'MSVC', 'Microsoft Planner', 'Make', 'IPython', 'Cockroachdb', 'Wikis', 'TiDB', 'Django', 'Redmine', 'Smartsheet', 'Firebase Realtime Database', 'BigQuery', 'Maven (build tool)', 'Ruff', 'Microsoft Azure', 'Fleet', 'Netlify', 'Objective-C'}

l=[]
o={}
k=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url='https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
for i in range(0,math.ceil(117/25)):

    res = requests.get(target_url.format(i))
    soup=BeautifulSoup(res.text,'html.parser')
    alljobs_on_this_page=soup.find_all("li")
    print(len(alljobs_on_this_page))
    for x in range(0,len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)

target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/'

print(l)




for j in range(0, len(l)):
    # time.sleep(2)
    jobID = l[j]
    checkingURL = target_url+jobID
    res=requests.get(checkingURL)
    soup=BeautifulSoup(res.text, 'html.parser')
    jobListing=soup.find_all("section")
    # jobDesc = soup.find("section",{"class":"show-more-less-html"})
    jobDesc = soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5 relative overflow-hidden"})
    o["jobID"]=jobID
    o["jobDesc"]=jobDesc
    k.append(o)
    o = {}
    


df = pd.DataFrame(k)
df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
print(k)

