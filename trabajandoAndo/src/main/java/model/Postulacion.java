package model;

public class Postulacion {
    private double contraOferta;
    private Trabajo trabajo;
    private Freelance freelance;

    public Postulacion(double contraOferta, Trabajo trabajo, Freelance freelance) {
        this.contraOferta = contraOferta;
        this.trabajo = trabajo;
        this.freelance = freelance;
    }

    public double getContraOferta() {
        return contraOferta;
    }

    public void setContraOferta(double contraOferta) {
        this.contraOferta = contraOferta;
    }

    public Trabajo getTrabajo() {
        return trabajo;
    }

    public void setTrabajo(Trabajo trabajo) {
        this.trabajo = trabajo;
    }

    public Freelance getFreelance() {
        return freelance;
    }

    public void setFreelance(Freelance freelance) {
        this.freelance = freelance;
    }
}
