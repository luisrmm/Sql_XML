CREATE TABLE Factura (
	Clave varchar(255) PRIMARY KEY,
    CodigoActividad varchar(255),
	NumeroConsecutivo varchar(255),
    FechaEmision varchar(255),
    EmisorNombre varchar(255),
    EmisorIdentificacionTipo varchar(255),
    EmisorIdentificacionNumuero varchar(255),
    EmisorUbicacionProvincia varchar(255),
    EmisorUbicacionCanton varchar(255),
    EmisorUbicacionDistrito varchar(255),
    EmisorUbicacionBarrio varchar(255),
	EmisorUbicacionOtrasSenas varchar(255),
	EmisorTelefonoCodigoPais varchar(255),
    EmisorTelefonoNumTelefono varchar(255),
    EmisorCorreoElectronico varchar(255),
    ReceptorNombre varchar(255),
    ReceptorIdentificacionTipo varchar(255),
    ReceptorIdentificacionNumero varchar(255),
    ReceptorCorreoElectronico varchar(255),
    CondicionVenta varchar(255),
    MedioPago varchar(255),
    ResumenFacturaCodigoTipoMonedaCodigoMoneda varchar(255),
    ResumenFacturaCodigoTipoMonedaTipoCambio varchar(255),
	ResumenFacturaTotalServGravados varchar(255),
    ResumenFacturaTotalServExentos varchar(255),
    ResumenFacturaTotalMercanciasGravadas varchar(255),
    ResumenFacturaTotalMercanciasExentas varchar(255),
    ResumenFacturaTotalGravado varchar(255),
    ResumenFacturaTotalExento varchar(255),
    ResumenFacturaTotalVenta varchar(255),
    ResumenFacturaTotalDescuentos varchar(255),
    ResumenFacturaTotalVentaNeta varchar(255),
	ResumenFacturaTotalImpuesto varchar(255),
	ResumenFacturaTotalComprobante varchar(255),
    OtrosOtroTexto varchar(255)
)

CREATE TABLE DetalleServicio (
	IdDetalleServicio int PRIMARY KEY KEY AUTO_INCREMENT,
    ClaveFacturaElectronica varchar(255),
    FOREIGN KEY (ClaveFacturaElectronica) REFERENCES factura(Clave),
	DetalleServicioLineaDetalleNumeroLinea varchar(255),
    DetalleServicioLineaDetalleCodigoComercioTipo varchar(255),
    DetalleServicioLineaDetalleCodigoComercioCodigo varchar(255),
    DetalleServicioLineaDetalleCantidad varchar(255),
    DetalleServicioLineaDetalleUnidadMedida varchar(255),
    DetalleServicioLineaDetalleDetalle varchar(255),
    DetalleServicioLineaDetallePrecioUnitario varchar(255),
    DetalleServicioLineaDetalleMontoTotal varchar(255),
    DetalleServicioLineaDetalleDescuentoMontoDescuento varchar(255),
    DetalleServicioLineaDetalleDescuentoNaturalezaDescuento varchar(255),
    DetalleServicioLineaDetalleSubtotal varchar(255),
    DetalleServicioLineaDetalleImpuestoCodigo varchar(255),
    DetalleServicioLineaDetalleImpuestoCodigoTarifa varchar(255),
    DetalleServicioLineaDetalleImpuestoTarifa varchar(255),
    DetalleServicioLineaDetalleImpuestoMonto varchar(255),
    DetalleServicioLineaDetalleImpuestoNeto varchar(255),
	DetalleServicioLineaDetalleMontoTotalLinea varchar(255)
)

DELETE FROM factura
WHERE Clave = '50614081900011121314500100001010000000027101002449';

DROP TABLE detalleservicio;