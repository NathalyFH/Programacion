#define LED 15 //Se define el pin del led

int frecuencia = 5000; //Se define la frecuencia inicial a la se trabajará
int resolucion = 8; //Se define la resolucion inicial
int resoluciond = 255; //Se define la resolucion inicial en valor analogico
int dutycyclep = 50; //Se define el dutycycle inicial en forma de porcentaje
int dutycycle = 127; //Se define el dutycycle inicial en forma de valor analogico
const int canal = 1; //Se define el canal en el cual se trabajará

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); //Inicia el serial
  pinMode(LED, OUTPUT); //Define el pin del led como una salida
  ledcAttachPin(LED, canal); //Se le asigna el canal al pin de salida
  ledcSetup(canal, frecuencia, resolucion); //Escribe la configuracion con nuestros valores iniciales
}

void loop() {
  // put your main code here, to run repeatedly:
    char option=Serial.read(); //Lee el primer caracter que ingresa en el serial
    int newpos=Serial.readStringUntil('\n').toInt(); //Lee los siguientes caracteres y los convierte en enteros
    switch(option)
    {
      case 'F':
      frecuencia=newpos; //Lee asigna el valor ingresado a frecuencia
      break;
      case 'R':
      if (newpos<=16 || newpos>=1){//Si la resolucion es de entre 1 y 16 bits, permititra cambiar la resolucion
        resolucion=newpos; //Le asigna los bits escritos
        resoluciond = (pow(2,resolucion)-1); //Convierte el valor de bits a su resolucion analogica
        dutycycle = ((dutycyclep*resoluciond)/100); //Hace que el dutycycle que estaba antes sea el mismo para la nueva resolucion
      }
      else{
        Serial.print("Defina una resolucion de entre 1 y 16 bits");
      }
      break;
      case 'D':
      if (newpos>=0 || newpos<=100){
        dutycycle = ((newpos*resoluciond)/100); //Toma el % del dutycycle ingresado y lo convierte al valor analogico respecto a la resolucion que tiene
        dutycyclep = newpos; //Sirve para despues imprimir el porcentaje ingresado
      }
      else{
        Serial.print("Defina un porcentaje de entre 0 y 100%");
      }
      break;
      default:
      Serial.println("Ingresa una de las opciones disponibles: F, R o D, seguido del valor deseado"); //Siempre esta imprimiendo las opciones para escribir
    }

    ledcChangeFrequency(canal,frecuencia,resolucion); //Cambia a la frecuencia y resolucion
    ledcWrite(canal,dutycycle); //Cambia el dutycycle
  
  Serial.println("Frecuencia: " + String(frecuencia) + "Hz");
  Serial.println("Duty Cycle: " + String(dutycyclep) + "%");
  Serial.println("Resolucion: " + String(resolucion) + " bits");
  delay(1000);
  }
