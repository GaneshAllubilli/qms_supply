import asyncio
from playwright.async_api import async_playwright
import os
import json
from datetime import datetime

async def explore_with_screenshots():
    """
    Improved exploration script that waits for user interaction
    to navigate through the application while automatically capturing screenshots.
    """
    async with async_playwright() as p:
        print("=" * 60)
        print("QMS EXPLORATION ASSISTANT")
        print("=" * 60)
        print("\nLaunching Edge browser...")
        
        try:
            browser = await p.chromium.launch(channel="msedge", headless=False, slow_mo=500)
        except Exception as e:
            executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            if os.path.exists(executable_path):
                browser = await p.chromium.launch(executable_path=executable_path, headless=False, slow_mo=500)
            else:
                executable_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
                browser = await p.chromium.launch(executable_path=executable_path, headless=False, slow_mo=500)

        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        output_dir = "qms_exploration_output"
        os.makedirs(output_dir, exist_ok=True)

        print(f"\n✓ Browser launched")
        print(f"✓ Output directory: {output_dir}/")
        
        # Navigate and login
        print("\n[1/7] Navigating to login page...")
        await page.goto("http://216.48.184.249:5274/quality", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(2)
        
        print("[2/7] Logging in...")
        try:
            # Fill login form
            await page.fill('input[type="email"]', "testing@aivoa.net")
            await page.fill('input[type="password"]', "password123")
            await page.screenshot(path=f"{output_dir}/01_login_filled.png", full_page=True)
            
            # Click login
            await page.click('button[type="submit"]')
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(3)
            
            # Capture dashboard
            await page.screenshot(path=f"{output_dir}/02_dashboard.png", full_page=True)
            html = await page.content()
            with open(f"{output_dir}/dashboard.html", "w", encoding="utf-8") as f:
                f.write(html)
            
            print("✓ Login successful!")
            print("✓ Dashboard captured")
            
        except Exception as e:
            print(f"✗ Login failed: {e}")
            await page.screenshot(path=f"{output_dir}/error_login.png", full_page=True)
            return
        
        # Interactive exploration
        print("\n" + "=" * 60)
        print("INTERACTIVE EXPLORATION MODE")
        print("=" * 60)
        print("\nInstructions:")
        print("1. Manually navigate to each QMS module in the browser")
        print("2. After navigating to a module, return to this terminal")
        print("3. Enter the module name to capture a screenshot")
        print("4. Type 'done' when finished exploring all modules")
        print("\nModules to explore:")
        print("  - Deviation Management")
        print("  - CAPA")
        print("  - Product Complaints")
        print("  - Recall Management")
        print("  - Adverse Event Reporting")
        print("  - Supplier Management")
        print("=" * 60)
        
        screenshot_count = 3
        captured_modules = []
        
        while True:
            module_name = input("\nEnter module name (or 'done' to finish): ").strip()
            
            if module_name.lower() == 'done':
                break
            
            if not module_name:
                continue
            
            # Capture screenshot
            filename = module_name.lower().replace(" ", "_")
            screenshot_path = f"{output_dir}/{screenshot_count:02d}_{filename}.png"
            html_path = f"{output_dir}/{filename}.html"
            
            await page.screenshot(path=screenshot_path, full_page=True)
            html = await page.content()
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            
            captured_modules.append({
                "name": module_name,
                "screenshot": screenshot_path,
                "html": html_path,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"✓ Captured: {module_name}")
            print(f"  Screenshot: {screenshot_path}")
            print(f"  HTML: {html_path}")
            
            screenshot_count += 1
        
        # Save exploration summary
        summary = {
            "exploration_date": datetime.now().isoformat(),
            "total_modules_captured": len(captured_modules),
            "modules": captured_modules
        }
        
        with open(f"{output_dir}/exploration_summary.json", "w") as f:
            json.dump(summary, f, indent=2)
        
        print("\n" + "=" * 60)
        print("EXPLORATION COMPLETE")
        print("=" * 60)
        print(f"\nTotal modules captured: {len(captured_modules)}")
        print(f"Output directory: {output_dir}/")
        print("\nFiles created:")
        print(f"  - {len(captured_modules)} screenshots")
        print(f"  - {len(captured_modules)} HTML files")
        print(f"  - 1 exploration summary (JSON)")
        print("\nPress Enter to close browser...")
        input()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_with_screenshots())
