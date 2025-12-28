import pymupdf  # Modern import for PyMuPDF
import os
import sys
from ollama_ocr import run_deepseek_ocr

def process_pdf_to_html_tables(pdf_path, output_dir='./output'):
    """
    Converts each page of a PDF to an image and extracts data using DeepSeek-OCR via Ollama.
    Focuses on extracting tables in HTML format.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the PDF
    doc = pymupdf.open(pdf_path)
    combined_results = []
    
    # Custom prompt to force HTML table output
    prompt = "<image>\n<|grounding|>Convert the document to markdown. Describe all images. Preserve structure of document."
        
    #prompt = "<image>\n<|grounding|>Convert the document to markdown."
  

    print(f"Starting processing for {pdf_path} ({len(doc)} pages)...")

    for page_num in range(len(doc)):
        print(f"Processing Page {page_num + 1}/{len(doc)}...")
        
        # Render page to an image (Grayscale)
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2, 2), colorspace=pymupdf.csGRAY)
        
        temp_image_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        pix.save(temp_image_path)
        
        # Run OCR
        
        page_result = run_deepseek_ocr(temp_image_path, prompt)
        
        if page_result:
            combined_results.append(f"<!-- Page {page_num + 1} -->\n{page_result}")
            
            # Optional: Save individual page markdown
            with open(os.path.join(output_dir, f"page_{page_num + 1}.md"), 'w', encoding='utf-8') as f:
                f.write(page_result)
        
        # Clean up temp image
        os.remove(temp_image_path)

    # Save combined results
    combined_output_path = os.path.join(output_dir, "combined_results.md")
    with open(combined_output_path, 'w', encoding='utf-8') as f:
        # Wrap in basic HTML structure if needed
        f.write("\n".join(combined_results))

    print(f"\nProcessing complete. Combined results saved to: {combined_output_path}")

if __name__ == "__main__":
    pdf_file = "deepseekocr.pdf"
    output_folder = "./deepseek_extraction"
    
    process_pdf_to_html_tables(pdf_file, output_folder)
