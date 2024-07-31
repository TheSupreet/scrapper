import requests
from bs4 import BeautifulSoup
import json

def get_project_details(project_url):
    """Fetch details from the project detail page."""
    print(f'Fetching details from: {project_url}')
    response = requests.get(project_url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        details = {}
        
        # Extract the required fields (Example, adjust selectors as needed)
        details['GSTIN No'] = soup.find('div', text='GSTIN No').find_next_sibling('div').text.strip()
        details['PAN No'] = soup.find('div', text='PAN No').find_next_sibling('div').text.strip()
        details['Name'] = soup.find('div', text='Name').find_next_sibling('div').text.strip()
        details['Permanent Address'] = soup.find('div', text='Permanent Address').find_next_sibling('div').text.strip()
        
        # Print the extracted details
        print(f'Details for {project_url}:')
        print(f'  GSTIN No: {details["GSTIN No"]}')
        print(f'  PAN No: {details["PAN No"]}')
        print(f'  Name: {details["Name"]}')
        print(f'  Permanent Address: {details["Permanent Address"]}')
        
        return details
    else:
        print(f'Failed to fetch details. Status code: {response.status_code}')
    return None

def main():
    url = 'https://hprera.nic.in/PublicDashboard'
    
    # Get the list of projects
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the list of projects (Adjust selector as needed)
        projects = soup.find_all('a', title='View Application', limit=6)
        print(f'Found {len(projects)} projects.')
        
        project_data = []
        for project in projects:
            project_url = project.get('href')
            if not project_url.startswith('http'):
                project_url = f'https://hprera.nic.in{project_url}'
            print(f'Processing Project URL: {project_url}')
            details = get_project_details(project_url)
            if details:
                project_data.append(details)
        
        # Save project data to JSON file
        with open('project_data.json', 'w') as f:
            json.dump(project_data, f, indent=4)
        
        print("Data scraped and saved to project_data.json.")
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

if __name__ == "__main__":
    main()
