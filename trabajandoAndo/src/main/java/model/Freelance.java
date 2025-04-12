package model;

public class Freelance extends Persona{
    private String lenguajes;
    private double precioHora;
    private int nivelAcademico;
    private int experiencia;
    private String idiomas;


    public Freelance(String nombre, String email, int id, String lenguajes, double precioHora, int nivelAcademico, int experiencia) {
        super(nombre, email, id);
        this.lenguajes = lenguajes;
        this.precioHora = precioHora;
        this.nivelAcademico = nivelAcademico;
        this.experiencia = experiencia;
    }

    public String getLenguajes() {
        return lenguajes;
    }

    public void setLenguajes(String lenguajes) {
        this.lenguajes = lenguajes;
    }

    public double getPrecioHora() {
        return precioHora;
    }

    public void setPrecioHora(double precioHora) {
        this.precioHora = precioHora;
    }

    public int getNivelAcademico() {
        return nivelAcademico;
    }

    public void setNivelAcademico(int nivelAcademico) {
        this.nivelAcademico = nivelAcademico;
    }

    public int getExperiencia() {
        return experiencia;
    }

    public void setExperiencia(int experiencia) {
        this.experiencia = experiencia;
    }

    public String getIdiomas() {
        return idiomas;
    }

    public void setIdiomas(String idiomas) {
        this.idiomas = idiomas;
    }
}


