print("BOT START")

try:
    from services.telegram import send
    print("IMPORT OK")

    send("TEST FROM GITHUB")
    print("SEND DONE")

except Exception as e:
    print("ERROR:", e)

print("BOT END")
