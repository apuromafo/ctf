import requests

def fetch_and_convert_glossary():
    url = "https://tryhackme.com/api/v2/glossary"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"[*] Fetching data from {url}...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") != "success":
            print("[!] API error.")
            return

        glossary_list = data.get("data", [])
        
        # Ordenar alfabéticamente por el término (Term)
        glossary_list.sort(key=lambda x: x.get("term", "").upper())

        md_output = "# TryHackMe Glossary\n\n"
        # Nueva cabecera con columna de número
        md_output += "| # | Term | Definition | Videos | Rooms | Articles |\n"
        md_output += "| --- | --- | --- | --- | --- | --- |\n"

        for index, entry in enumerate(glossary_list, start=1):
            term = entry.get("term", "N/A")
            definition = entry.get("definition", "N/A").replace("\n", " ").replace("\r", "")
            
            res = entry.get("resources", {})
            
            # Videos
            v_list = res.get("videos", [])
            videos = "<br>".join([f"[Video]({v})" for v in v_list]) if v_list else "-"
            
            # Rooms
            r_list = res.get("roomCodes", [])
            rooms = "<br>".join([f"[{r}](https://tryhackme.com/room/{r})" for r in r_list]) if r_list else "-"
            
            # Articles
            a_list = res.get("articles", [])
            articles = "<br>".join([f"[Link]({a})" for a in a_list]) if a_list else "-"

            # Fila con el índice (numero)
            md_output += f"| {index} | **{term}** | {definition} | {videos} | {rooms} | {articles} |\n"

        with open("glossary.md", "w", encoding="utf-8") as f:
            f.write(md_output)
        
        print(f"[+] Success! {len(glossary_list)} terms saved to 'glossary.md'.")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    fetch_and_convert_glossary()