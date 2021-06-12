
namespace ClienteFactura
{
    partial class Factura
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblFactura = new System.Windows.Forms.Label();
            this.btnFactura = new System.Windows.Forms.Button();
            this.datosFacturatxt = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // lblFactura
            // 
            this.lblFactura.AutoSize = true;
            this.lblFactura.Location = new System.Drawing.Point(274, 20);
            this.lblFactura.Name = "lblFactura";
            this.lblFactura.Size = new System.Drawing.Size(230, 20);
            this.lblFactura.TabIndex = 0;
            this.lblFactura.Text = "Pulse el boton para ver la factura.";
            // 
            // btnFactura
            // 
            this.btnFactura.Location = new System.Drawing.Point(273, 53);
            this.btnFactura.Name = "btnFactura";
            this.btnFactura.Size = new System.Drawing.Size(231, 29);
            this.btnFactura.TabIndex = 1;
            this.btnFactura.Text = "Mostrar Factura";
            this.btnFactura.UseVisualStyleBackColor = true;
            this.btnFactura.Click += new System.EventHandler(this.btnFactura_Click);
            // 
            // datosFacturatxt
            // 
            this.datosFacturatxt.Location = new System.Drawing.Point(12, 88);
            this.datosFacturatxt.Name = "datosFacturatxt";
            this.datosFacturatxt.ReadOnly = true;
            this.datosFacturatxt.Size = new System.Drawing.Size(776, 481);
            this.datosFacturatxt.TabIndex = 2;
            this.datosFacturatxt.Text = "";
            // 
            // Factura
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 581);
            this.Controls.Add(this.datosFacturatxt);
            this.Controls.Add(this.btnFactura);
            this.Controls.Add(this.lblFactura);
            this.Name = "Factura";
            this.Text = "Factura";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblFactura;
        private System.Windows.Forms.Button btnFactura;
        private System.Windows.Forms.RichTextBox datosFacturatxt;
    }
}

