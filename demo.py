from campana import Campana
from anuncio import Video, Anuncio # Necesitamos Anuncio para llamar a mostrar_formatos estático
from error import LargoExcedidoException, SubTipoInvalidoException
from apoyo_prueba import FORMATOS_ANUNCIOS # Importa los datos de apoyo
from datetime import date
import os # Para verificar si el archivo de log existe

# Define el nombre del archivo de log de errores.
ERROR_LOG_FILE = "error.log"

def log_error(message: str):
    """
    Función para escribir mensajes de error en el archivo error.log. 
    Añade la fecha actual al mensaje.
    """
    with open(ERROR_LOG_FILE, "a") as f: # Abre en modo 'append' para añadir al final.
        f.write(f"{date.today()}: {message}\n")

if __name__ == "__main__":
    # Mostrar formatos disponibles al inicio. 
    print("--- Formatos de Anuncios Disponibles ---")
    Anuncio.mostrar_formatos(FORMATOS_ANUNCIOS)
    print("-" * 40)

    # Datos para crear una campaña con solo 1 anuncio de tipo Video. 
    anuncios_para_campana = [
        {
            "tipo": "Video",
            "url_archivo": "http://example.com/video_promo.mp4",
            "url_clic": "http://example.com/click_video",
            "duracion": 45
        }
    ]

    # Crear una instancia de Campaña. 
    try:
        mi_campana = Campana(
            nombre="Mi Primera Campaña Digital",
            fecha_inicio=date(2025, 7, 1),
            fecha_termino=date(2025, 12, 31),
            anuncios_data=anuncios_para_campana
        )
        print("Campaña creada exitosamente.")
        print(mi_campana) # Imprime la información de la campaña usando __str__. 
    except Exception as e:
        print(f"Error al crear la campaña inicial: {e}")
        log_error(f"Error de inicialización de campaña: {e}")
        exit() # Sale si la campaña no se puede crear


    print("\n--- Modificando la Campaña ---")

    # Solicitar y modificar el nombre de la campaña. 
    nuevo_nombre_campana = input("Ingrese el nuevo nombre para la campaña (max 250 chars): ")
    try:
        mi_campana.nombre = nuevo_nombre_campana
        print(f"Nombre de la campaña actualizado a: '{mi_campana.nombre}'")
    except LargoExcedidoException as e:
        print(f"ERROR: {e.message}")
        log_error(f"LargoExcedidoException en nombre de campaña: {e.message}")
    except Exception as e:
        print(f"ERROR inesperado al cambiar el nombre: {e}")
        log_error(f"Error inesperado al cambiar nombre: {e}")

    print("-" * 40)

    # Solicitar y modificar el sub_tipo del primer anuncio (que sabemos es Video). 
    # Se asume que siempre habrá al menos un anuncio de tipo Video según la consigna. 
    if mi_campana.anuncios and isinstance(mi_campana.anuncios[0], Video):
        primer_anuncio_video = mi_campana.anuncios[0]
        print(f"Subtipos permitidos para Video: {Video.SUB_TIPOS}")
        nuevo_sub_tipo_anuncio = input(f"Ingrese el nuevo subtipo para el anuncio de video (actual: '{primer_anuncio_video.sub_tipo}'): ")
        try:
            primer_anuncio_video.sub_tipo = nuevo_sub_tipo_anuncio
            print(f"Subtipo del anuncio actualizado a: '{primer_anuncio_video.sub_tipo}'")
        except SubTipoInvalidoException as e:
            print(f"ERROR: {e.message}")
            log_error(f"SubTipoInvalidoException en subtipo de anuncio: {e.message}")
        except Exception as e:
            print(f"ERROR inesperado al cambiar el subtipo: {e}")
            log_error(f"Error inesperado al cambiar subtipo: {e}")
    else:
        print("No se encontró un anuncio de tipo Video en la campaña para modificar su subtipo.")

    print("-" * 40)
    print("\n--- Estado Final de la Campaña ---")
    print(mi_campana)

    # Demostración de métodos abstractos (aunque solo imprimen mensajes)
    print("\n--- Demostración de métodos de Anuncio ---")
    for i, anuncio in enumerate(mi_campana.anuncios):
        print(f"\nProcesando Anuncio {i+1} ({anuncio.FORMATO}):")
        anuncio.comprimir_anuncio()
        anuncio.redimensionar_anuncio()