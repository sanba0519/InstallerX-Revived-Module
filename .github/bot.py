from telethon import TelegramClient, sessions
import asyncio
import os
import sys

# --- Environment Variables ---
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
_chat_id_raw = os.environ.get("CHAT_ID", "")
BOT_CI_SESSION = os.environ.get("BOT_CI_SESSION")

# Parse CHAT_ID - support both numeric IDs and usernames
if _chat_id_raw:
    # If it starts with @ or is not numeric, treat as username
    if _chat_id_raw.startswith('@') or not _chat_id_raw.lstrip('-').isdigit():
        CHAT_ID = _chat_id_raw
    else:
        CHAT_ID = int(_chat_id_raw)
else:
    CHAT_ID = None

async def send_telegram_files(files):
    """
    Connects to Telegram and sends the specified files as a group message.
    """
    # Filter out empty file paths
    files = [f for f in files if f and os.path.exists(f)]

    if not files:
        print("[-] No valid files to upload")
        return

    session = sessions.StringSession(BOT_CI_SESSION)

    async with TelegramClient(session, api_id=API_ID, api_hash=API_HASH) as client:
        # Start the client with the bot token
        await client.start(bot_token=BOT_TOKEN)

        print(f"[+] Sending {len(files)} file(s) as a group...")
        print(f"[+] Target chat: {CHAT_ID}")

        # Send the files together as an album/group
        await client.send_file(
            entity=CHAT_ID,
            file=files,
        )
        print("[+] Files sent successfully.")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if CHAT_ID is None:
            print("[-] CHAT_ID is not set, cannot send files")
            sys.exit(1)
        # Get all file paths from command-line arguments
        apk_files = sys.argv[1:]
        print(f"[+] Found files to upload: {apk_files}")
        try:
            # Run the asynchronous function
            asyncio.run(send_telegram_files(apk_files))
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        print("[-] No file paths provided as arguments.")
    else:
        print("[-] No file paths provided as arguments.")