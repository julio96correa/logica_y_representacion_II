package model;

public class Contrato {
   private double nroContrato;
   private Freelance freelance;
   private double pagoFinal;
   private Trabajo trabajo;

   public Contrato(double nroContrato, Freelance freelance, Trabajo trabajo, double pagoFinal) {
       this.nroContrato = nroContrato;
       this.freelance = freelance;
       this.trabajo = trabajo;
       this.pagoFinal = pagoFinal;
   }
}
