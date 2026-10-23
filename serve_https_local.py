from rrserver import create_app
from setup_local_certificate import ensure_local_certificate
import os
from dotenv import load_dotenv

# Load the variables from your .env file
load_dotenv()

if __name__ == "__main__":
    certificate, key, _ = ensure_local_certificate()
    
    app = create_app({
        # os.getenv reads the value. The second argument is a fallback if .env is missing it.
        "RECNET_DOMAIN": os.getenv("RECNET_DOMAIN"),
        "SINGLE_HOST_MODE": True,
    })
    
    print("Local server: https://127.0.0.1:5051", flush=True)
    app.run(
        host="127.0.0.1",
        port=5051,
        threaded=True,
        use_reloader=False,
        ssl_context=(str(certificate), str(key)),
    )
