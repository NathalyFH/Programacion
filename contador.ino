// Cronómetro
unsigned long inicio, finalizado, Ttranscurrido;

const int BOTON=34;
int val;
void setup() 
{
  Serial.begin(9600);
  pinMode(BOTON, INPUT); // Boton de inicio y parar
  Serial.println("Presione el pulsador para Inicio/reset y para detener tiempo transcurrido"); 
  } 
  void MostrarResultado() 
  { 
    float h, m, s, ms;
    unsigned long terminado; 
    Ttranscurrido = finalizado - inicio;
    h = int(Ttranscurrido / 3600000);
    terminado = Ttranscurrido % 3600000; 
    m = int(terminado / 60000);
    terminado = terminado % 60000;
    s = int(terminado / 1000);
    ms = terminado % 1000; 
    Serial.print("Tiempo transcurrido : "); 
    Serial.println(Ttranscurrido);
    Serial.print("Tiempo transcurrido detallado: ");
    Serial.print(h, 0);
    Serial.print("h ");
    Serial.print(m, 0);
    Serial.print("m ");
    Serial.print(s, 0);
    Serial.print("s ");
    Serial.print(ms, 0);
    Serial.println("ms");
    Serial.println();
    }
    void loop()
    {
      val=digitalRead(BOTON);
      if (val== HIGH)
      { 
       inicio = millis();
       delay(300); //  por rebote 
       Serial.println("Inicializar...");
      } 
      else (digitalRead(BOTON) == LOW);
      { 
        finalizado = millis();
        delay(300); // por rebote 
        MostrarResultado(); 
       }
}
