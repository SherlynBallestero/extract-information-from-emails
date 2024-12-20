# Extract Information from Emails

This project allows you to extract information from specific emails using the Gmail API. It filters emails containing order tracking information and saves the data in JSON files.

## Requirements

Make sure you have Python installed and the following libraries:

- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- tkinter

You can install the dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Configuration

1. **Google Credentials**: 
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Gmail API.
   - Configure the OAuth 2.0 consent screen.
   - Create OAuth 2.0 credentials and download the `credentials.json` file.
   - Save the `credentials.json` file in the project directory.

## Usage

1. **Run the Main Script**:
   - Run the main.py  script to start the authentication and email extraction process.

```bash
python main.py
```

2. **Graphical Interface (Optional)**:
   - Run the app.py script to use the Tkinter-based graphical interface.

```bash
python app.py
```

## Project Structure

- main.py : Main script that handles authentication and email extraction.
- app.py : Graphical interface to interact with the main script.
- requirements.txt : File with the necessary dependencies.
- `credentials.json`: Google credentials file (not included in the repository).
- `token.pickle`: File that stores access and refresh tokens (generated automatically, also not included in the repo).

## Security

- **Protect Credential Files**: Ensure that the `token.pickle` and `credentials.json` files are in secure locations with appropriate permissions, revoke tokens if necessary.

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you wish to make.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.






