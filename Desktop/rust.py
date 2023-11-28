import cv2
import numpy as np
from tensorflow.keras.models import load_model

def predict_image(model, img):
    img = cv2.resize(img, (150, 150))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return prediction

# Cargar el modelo
model_path = r".\Entrega Final\Cliente\Video y Joy\pesos.h5"
loaded_model = load_model(model_path)

# Inicializar la captura de video
cap = cv2.VideoCapture(1)  # 0 es generalmente la cámara integrada

while True:
    # Capturar marco por marco
    ret, frame = cap.read()

    if not ret:
        break

    # Realizar la detección
    prediction = predict_image(loaded_model, frame)

    # Determinar la clasificación y la probabilidad
    if prediction < 0.5:
        classification = "No Corrosion"
        probability = 1 - prediction[0][0]
    else:
        classification = "Corrosion"
        probability = prediction[0][0]

    # Mostrar la clasificación y la probabilidad en el marco
    cv2.putText(frame, f"Classification: {classification}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Probability: {probability:.2f}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el marco
    cv2.imshow('Frame', frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
