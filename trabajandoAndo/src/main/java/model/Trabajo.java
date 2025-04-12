package model;

public class Trabajo {
    private Empresa empresa;
    private String lenguaje;
    private int tiempo;
    private String descripcion;
    private String idioma;
    private double pago;
    private boolean negociable;
    private int disponibilidad;
    private int experiencia;

    public Trabajo(Empresa empresa, String lenguaje, int tiempo, String descripcion, String idioma, double pago, boolean negociable, int disponibilidad, int experiencia) {
        this.empresa = empresa;
        this.lenguaje = lenguaje;
        this.tiempo = tiempo;
        this.descripcion = descripcion;
        this.idioma = idioma;
        this.pago = pago;
        this.negociable = negociable;
        this.disponibilidad = disponibilidad;
        this.experiencia = experiencia;
    }

    public Empresa getEmpresa() {
        return empresa;
    }

    public void setEmpresa(Empresa empresa) {
        this.empresa = empresa;
    }

    public String getLenguaje() {
        return lenguaje;
    }

    public void setLenguaje(String lenguaje) {
        this.lenguaje = lenguaje;
    }

    public int getTiempo() {
        return tiempo;
    }

    public void setTiempo(int tiempo) {
        this.tiempo = tiempo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getIdioma() {
        return idioma;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public double getPago() {
        return pago;
    }

    public void setPago(double pago) {
        this.pago = pago;
    }

    public boolean isNegociable() {
        return negociable;
    }

    public void setNegociable(boolean negociable) {
        this.negociable = negociable;
    }

    public int getDisponibilidad() {
        return disponibilidad;
    }

    public void setDisponibilidad(int disponibilidad) {
        this.disponibilidad = disponibilidad;
    }

    public int getExperiencia() {
        return experiencia;
    }

    public void setExperiencia(int experiencia) {
        this.experiencia = experiencia;
    }
}
