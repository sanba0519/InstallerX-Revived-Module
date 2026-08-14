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


async def send_telegram_text(text, target):
    """
    Sends a plain text message to the specified user or chat.
    """
    session = sessions.StringSession(BOT_CI_SESSION)

    async with TelegramClient(session, api_id=API_ID, api_hash=API_HASH) as client:
        # Start the client with the bot token
        await client.start(bot_token=BOT_TOKEN)

        print(f"[+] Sending text message to: {target}")
        await client.send_message(entity=target, message=text)
        print("[+] Message sent successfully.")


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("[-] No arguments provided.")
        sys.exit(1)

    # Text message mode: bot.py --text "message" [--to user_or_chat_id]
    if args[0] == '--text':
        text = None
        target = CHAT_ID
        i = 1
        while i < len(args):
            if args[i] == '--to':
                raw = args[i + 1] if i + 1 < len(args) else None
                if raw is not None:
                    if raw.lstrip('-').isdigit():
                        target = int(raw)
                    else:
                        target = raw
                i += 2
            else:
                text = args[i]
                i += 1
        if not text:
            print("[-] No text message provided.")
            sys.exit(1)
        if target is None:
            print("[-] Target not set, cannot send message")
            sys.exit(1)
        try:
            asyncio.run(send_telegram_text(text, target))
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    # File upload mode (backward compatible)
    else:
        if CHAT_ID is None:
            print("[-] CHAT_ID is not set, cannot send files")
            sys.exit(1)
        # Get all file paths from command-line arguments
        apk_files = args
        print(f"[+] Found files to upload: {apk_files}")
        try:
            # Run the asynchronous function
            asyncio.run(send_telegram_files(apk_files))
        except Exception as e:
            print(f"[-] An error occurred: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)