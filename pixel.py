from PIL import Image

def converter_e_contar_pixels(caminho_entrada, caminho_saida):

  try:
        
        with Image.open(caminho_entrada) as img:
            # Converte a imagem ('1' para = 1-bit pixels, black and white) e ('L' para = monocromatico)
            img_mono = img.convert('L')

            img_mono.save(caminho_saida)
            print(f"Imagem convertida com sucesso e salva em: {caminho_saida}")

            print("\n--- Análise da Nova Imagem Monocromática ---")

            # Get pixel data directly from the converted image object in memory
            pixels = list(img_mono.getdata())

            # Calculate total pixels
            total_pixels = len(pixels)
            


            white_pixel_value = 255
            white_pixel_count = pixels.count(white_pixel_value)

            print(f"Dimensões: {img_mono.width} x {img_mono.height} pixels")
            print(f"Total de pixels: {total_pixels:,}".replace(",", "."))
            print(f"Total de pixels BRANCOS: {white_pixel_count:,}".replace(",", "."))

    except FileNotFoundError:
        print(f"Error: The input file '{caminho_entrada}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Início do Programa ---
if __name__ == "__main__":

    caminho_da_imagem_original = 'imagem.tif' 
    #caminho_da_imagem_convertida = 'resultado_monocromatico.png'
    #converter_e_contar_pixels(caminho_da_imagem_original, caminho_da_imagem_convertida)
