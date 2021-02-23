from fpdf import FPDF 
   
PDF = FPDF()    
PDF.add_page() 
PDF.set_font("Arial", size = 15) 
file = open("pp.txt", "r") 
  
for x in file: 
    PDF.cell(200, 10, txt = x, ln = 1, align = 'C') 
   
# save the pdf with name .pdf 
PDF.output("result.pdf")