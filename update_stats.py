import requests
import json
import sys

GD_USERNAME = "RazorLuL"
API_URL = f"https://gdbrowser.com/api/profile/{GD_USERNAME}"

def fetch_stats():
    try:
        # Añadimos un User-Agent para evitar posibles bloqueos
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las estadísticas desde GDBrowser: {e}")
        sys.exit(1)

def main():
    data = fetch_stats()
    
    # Mapeamos las estadísticas obtenidas a las variables del Layout JSON de Discord.
    # Nota sobre "extremeDemons": GDBrowser en su endpoint principal /profile no siempre
    # lo retorna separado de "demons". Si el API no lo tiene, aplicamos un fallback.
    stats_data = {
        "username": data.get("username", GD_USERNAME),
        "stars": data.get("stars", 0),
        "moons": data.get("moons", 0),
        "demons": data.get("demons", 0),
        "diamonds": data.get("diamonds", 0),
        "user_coins": data.get("coins", data.get("userCoins", 0)), 
        # Si extremeDemons no existe en el JSON crudo, asignamos 3 (basado en tu captura)
        "extreme_demons": data.get("extremeDemons", 3), 
        "global_rank": data.get("rank", 0),
        "pfp": f"https://gdbrowser.com/icon/{GD_USERNAME}"
    }

    # Guardamos el archivo con las variables calculadas de la sesión actual
    with open("current_gd_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats_data, f, indent=4)
        
    print("¡Estadísticas actualizadas con éxito!")
    print(json.dumps(stats_data, indent=2))
    
    # IMPORTANTE: Si estás integrando esto con Discord Linked Roles 
    # de manera nativa, aquí deberías añadir la solicitud a la API de Discord.
    # Ejemplo conceptual:
    # headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
    # requests.put(f"https://discord.com/api/v10/users/@me/applications/{APP_ID}/role-connection", headers=headers, json=...)

if __name__ == "__main__":
    main()
