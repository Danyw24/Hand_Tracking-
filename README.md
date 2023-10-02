# Hand Tracking Controller

## Autor
- Danyw24

## Descripción
Este proyecto implementa un controlador de seguimiento de manos utilizando Python 3.9.11. Puedes utilizar este controlador para interactuar con otros dispositivos o aplicaciones mediante gestos de manos detectados por una cámara.

## Componentes Utilizados
- Cámara (webcam o cámara externa)
- Arduino (opcional)
- Atmega328p
- Módulo NRF24L01 (opcional)
- Bibliotecas Python: `serialController`, `terminalGUI`, `HandsTrack`, `colorama`, `cv2` (OpenCV)

## Configuración
- Asegúrate de tener una cámara conectada y configurada correctamente en tu sistema.
- Si deseas controlar un dispositivo externo (como un dron), asegúrate de que el Arduino esté conectado a través de un puerto serie (como "/dev/ttyUSB0") y configurado con la velocidad de transmisión adecuada (por ejemplo, 9600 baudios).
- Puedes ajustar la configuración de la cámara cambiando las variables `CAM`, `WIDTH`, y `HEIGHT` en el código.

## Funcionalidades
Este controlador de seguimiento de manos permite interactuar con dispositivos o aplicaciones a través de gestos de manos detectados por la cámara. Algunas de las funcionalidades incluyen:

- Detección de manos en tiempo real.
- Cálculo de la velocidad de fotogramas (FPS) y visualización en pantalla.
- Control de dispositivos externos (por ejemplo, un dron) a través de comandos enviados a través de Arduino y el módulo NRF24L01 (opcional).
- Reconocimiento de gestos como toques y movimientos de dedos.

## Uso
1. Asegúrate de tener todos los componentes conectados y configurados según las especificaciones.
2. Ejecuta el script Python en un entorno compatible.
3. Utiliza tus manos frente a la cámara para interactuar con los dispositivos o aplicaciones.


## Notas
- Este proyecto es ideal para experimentar con la interacción gestual y el control de dispositivos utilizando el seguimiento de manos.
- Asegúrate de tener instaladas las bibliotecas Python requeridas en tu entorno de desarrollo.

---
