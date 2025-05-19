import requests
import json
import os
import glob

# Define the API endpoint
url = "https://texviewer.herokuapp.com/upload.php?uid=7a00162b-78e5-4dce-8a63-68b007bd7193"

# Headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8",
    "Connection": "keep-alive",
    "Origin": "https://texviewer.herokuapp.com",
    "Referer": "https://texviewer.herokuapp.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

# Output directory
output_dir = "final outputs"
os.makedirs(output_dir, exist_ok=True)

# Find all .tex files in the current directory (no subdirectories)
tex_files = [f for f in glob.glob("*.tex") if os.path.isfile(f)]
if not tex_files:
    print("No .tex files found in the current directory.")
    exit(1)

for tex_file in tex_files:
    print(f"\nProcessing {tex_file}...")

    # Load LaTeX document
    try:
        with open(tex_file, "r", encoding="utf-8") as file:
            latex_document = file.read()
        print(f"Successfully loaded {tex_file}")
    except Exception as e:
        print(f"Error reading {tex_file}: {e}")
        print(f"Skipping {tex_file}")
        continue

    # Form-data payload
    data = {
        "uid": "7a00162b-78e5-4dce-8a63-68b007bd7193",
        "texts": latex_document,
        "nonstopmode": "1",
        "title": os.path.splitext(os.path.basename(tex_file))[0]
    }

    try:
        # Send POST request
        print("Sending texts as raw text...")
        response = requests.post(url, headers=headers, data=data)

        # Check response status
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Response received successfully.")
            try:
                # Parse JSON response
                result = response.json()
                print("Response JSON:", json.dumps(result, indent=2))

                # Check for resultfile
                resultfile = result.get("resultfile")
                if resultfile:
                    # Construct URL for resultfile
                    resultfile_url = f"https://texviewer.herokuapp.com/{resultfile.replace('\\', '/')}"
                    print(f"Attempting to fetch resultfile: {resultfile_url}")

                    # GET request for resultfile
                    result_response = requests.get(resultfile_url)
                    if result_response.status_code == 200:
                        # Check Content-Type
                        content_type = result_response.headers.get("Content-Type", "")
                        print(f"Resultfile Content-Type: {content_type}")

                        # Save result file (overwrites if exists)
                        result_filename = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(tex_file))[0]}_result.txt")
                        if os.path.exists(result_filename):
                            print(f"Overwriting existing file: {result_filename}")
                        try:
                            with open(result_filename, "wb") as f:
                                f.write(result_response.content)
                            print(f"Result file saved as {result_filename}")
                        except IOError as e:
                            print(f"Error writing {result_filename}: {e}")
                            continue

                        # Parse result file JSON
                        if "text" in content_type:
                            try:
                                result_json = json.loads(result_response.text)
                                print("Result file JSON:", json.dumps(result_json, indent=2))

                                # Check for pdfname
                                pdf_url = result_json.get("pdfname")
                                if pdf_url:
                                    print(f"Attempting to fetch PDF: {pdf_url}")
                                    pdf_response = requests.get(pdf_url)
                                    if pdf_response.status_code == 200 and "application/pdf" in pdf_response.headers.get("Content-Type", ""):
                                        pdf_filename = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(tex_file))[0]}.pdf")
                                        if os.path.exists(pdf_filename):
                                            print(f"Overwriting existing file: {pdf_filename}")
                                        try:
                                            with open(pdf_filename, "wb") as f:
                                                f.write(pdf_response.content)
                                            print(f"PDF saved as {pdf_filename}")
                                        except IOError as e:
                                            print(f"Error writing {pdf_filename}: {e}")
                                            continue
                                    else:
                                        print(f"PDF fetch failed for {tex_file}. Status: {pdf_response.status_code}")
                                        print(f"Response: {pdf_response.text}")
                                else:
                                    print(f"No pdfname found in result file JSON for {tex_file}")
                            except json.JSONDecodeError:
                                print(f"Result file is not valid JSON for {tex_file}:", result_response.text[:1000])
                        else:
                            print(f"Result file is not text for {tex_file}; cannot parse for pdfname")
                    else:
                        print(f"Failed to fetch resultfile for {tex_file}. Status: {result_response.status_code}")
                        print(f"Response: {result_response.text}")
                else:
                    print(f"No resultfile found in response JSON for {tex_file}")

            except ValueError:
                print(f"Response is not valid JSON for {tex_file}:", response.text)
        else:
            print(f"Request failed for {tex_file}. Status: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error during request for {tex_file}: {e}")

print(f"\nProcessing complete. Check '{output_dir}' for results.")