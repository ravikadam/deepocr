import ollama
import os
import base64

def run_deepseek_ocr(image_path, prompt, output_path=None):
    """
    Runs DeepSeek-OCR using locally running Ollama.
    
    Args:
        image_path (str): Path to the image file.
        prompt (str): The prompt for OCR.
        output_path (str, optional): Directory to save the output markdown. Defaults to None.
    
    Returns:
        str: The OCR result text.
    """
    
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None

    print(f"Processing {image_path}...")
    
    try:
        response = ollama.generate(
            model='deepseek-ocr:latest',
            prompt=prompt,
            images=[image_path],
            stream=False
        )
        
        result = response['response']
        
        if output_path:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
            output_file = os.path.join(output_path, os.path.basename(image_path).rsplit('.', 1)[0] + '.md')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Result saved to: {output_file}")
            
        return result

    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) > 1:
        image_file = sys.argv[1]
    else:
        image_file = './page_1.png'
        
    output_dir = './'
    prompt = "<image>\nParse all charts and tables. Extract data as HTML document.Do not add <|ref|> and <det> prompts."
    #prompt = "<image>\n<|grounding|>Convert the document to markdown. "
    
    run_deepseek_ocr(image_file, prompt, output_dir)
