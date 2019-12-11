import shapefile

class Kedua:

    def __init__(self):
        self.kedua = shapefile.Writer('kedua', shapeType = shapefile.POLYGON)
        self.kedua.shapeType
        self.kedua.field('nama_ruangan', 'C')

    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, -2], [4, -2], [4, 1], [-3, 1], [-3, -2]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, -2], [29, -2], [29, 1], [22, 1], [22, -2]]])

    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 40], [4, 40], [4, 43], [-3, 43], [-3, 40]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 40], [29, 40], [29, 43], [22, 43], [22, 40]]])

    #Luthfi Muhammad Nabil - 1174035
    def tamanKosongTengah(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 11], [19, 11], [19, 30], [7, 30], [7, 11]]])

    #Hagan Rowlenstino - 1174040
    def R213(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 40], [10, 40], [10, 33], [7, 33], [7, 40]]])
        
    #Hagan Rowlenstino - 1174040
    def IRC(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[10, 40], [13, 40], [13, 33], [10, 33], [10, 40]]])

    #Hagan Rowlenstino - 1174040
    def RLabBisnis(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[13, 40], [16, 40], [16, 33], [13, 33], [13, 40]]])

    #Hagan Rowlenstino - 1174040
    def RLabComprehensive(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[16, 40], [19, 40], [19, 33], [16, 33], [16, 40]]])
        
    #Pasang fungsi baru diatas close()
    def close(self):
        self.kedua.close()