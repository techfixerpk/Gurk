# Nexus Titan V6 - Backend Processor
# Protocol: Universal 600 | Logic: Native OpenCV Enhancement

import cv2
import numpy as np
import os
import gc

class ImageProcessor:
    def __init__(self):
        self.output_dir = "enhanced_output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def enhance_image(self, image_path):
        # 1. Loading Image with Memory Management (4GB Optimisation)
        img = cv2.imread(image_path)
        if img is None:
            return "Error: Image not found."

        # 2. De-noising (Heavy Look)
        # Non-Local Means Denoising algorithm for cleaner research images
        denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        # 3. Local Contrast Enhancement (CLAHE)
        # Is se details bohot "sharp" aur "deep" nazar aati hain
        lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        enhanced_lab = cv2.merge((cl,a,b))
        enhanced_img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

        # 4. Sharpening Kernel (Reconstruction Protocol)
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        final_img = cv2.filter2D(enhanced_img, -1, kernel)

        # 5. Save & Memory Flush
        output_path = os.path.join(self.output_dir, "enhanced_" + os.path.basename(image_path))
        cv2.imwrite(output_path, final_img)
        
        # Explicit Garbage Collection for 4GB RAM stability
        del img, denoised, enhanced_img, final_img
        gc.collect()
        
        return output_path

# Integration Logic for Batch Processing
if __name__ == "__main__":
    print("[NEXUS TITAN] Processor Engine Active.")
    print("[PROTOCOL] Native Logic Enabled. Ready for Pixel Reconstruction.")
    # Example usage:
    # engine = ImageProcessor()
    # engine.enhance_image("sample.jpg")
  
