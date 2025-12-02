import asyncio
from playwright.async_api import async_playwright
import os
import json
from datetime import datetime

async def main():
    async with async_playwright() as p:
        print("Launching Edge...")
        try:
            browser = await p.chromium.launch(channel="msedge", headless=False)
        except Exception as e:
            print(f"Failed with channel='msedge': {e}")
            executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            if os.path.exists(executable_path):
                browser = await p.chromium.launch(executable_path=executable_path, headless=False)
            else:
                executable_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
                browser = await p.chromium.launch(executable_path=executable_path, headless=False)

        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        # Create output directory
        output_dir = "qms_exploration_output"
        os.makedirs(output_dir, exist_ok=True)

        exploration_log = []

        def log_step(step_name, details=""):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = {"timestamp": timestamp, "step": step_name, "details": details}
            exploration_log.append(log_entry)
            print(f"[{timestamp}] {step_name}: {details}")

        try:
            # Navigate to login page
            log_step("Navigation", "Going to login page")
            await page.goto("http://216.48.184.249:5274/quality", timeout=60000)
            await page.wait_for_load_state("networkidle", timeout=30000)
            await page.screenshot(path=f"{output_dir}/01_login_page.png", full_page=True)
            
            # Try to find and fill login form
            log_step("Login", "Looking for login form")
            await asyncio.sleep(2)  # Wait for React to render
            
            # Try multiple selectors for email/username
            email_selectors = [
                'input[type="email"]',
                'input[type="text"]',
                'input[name="email"]',
                'input[name="username"]',
                'input[placeholder*="email" i]',
                'input[placeholder*="username" i]'
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    email_input = await page.wait_for_selector(selector, timeout=5000)
                    if email_input:
                        log_step("Login", f"Found email input with selector: {selector}")
                        break
                except:
                    continue
            
            if not email_input:
                log_step("Error", "Could not find email input field")
                await page.screenshot(path=f"{output_dir}/error_no_email_field.png", full_page=True)
                return
            
            # Fill email
            await email_input.fill("testing@aivoa.net")
            log_step("Login", "Filled email field")
            
            # Find password field
            password_input = await page.wait_for_selector('input[type="password"]', timeout=5000)
            await password_input.fill("password123")
            log_step("Login", "Filled password field")
            
            await page.screenshot(path=f"{output_dir}/02_credentials_filled.png", full_page=True)
            
            # Find and click login button
            login_button_selectors = [
                'button[type="submit"]',
                'button:has-text("Sign In")',
                'button:has-text("Login")',
                'button:has-text("Log In")',
                'input[type="submit"]'
            ]
            
            for selector in login_button_selectors:
                try:
                    login_button = await page.wait_for_selector(selector, timeout=2000)
                    if login_button:
                        log_step("Login", f"Found login button: {selector}")
                        await login_button.click()
                        break
                except:
                    continue
            
            log_step("Login", "Clicked login button")
            await page.wait_for_load_state("networkidle", timeout=30000)
            await asyncio.sleep(3)
            await page.screenshot(path=f"{output_dir}/03_after_login.png", full_page=True)
            
            # Explore In-Process Quality - Deviation Management
            log_step("Navigation", "Exploring Deviation Management")
            
            # Try to find navigation menu
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            log_step("Navigation", f"Found {len(nav_items)} navigation items")
            
            # Look for Deviation Management
            for item in nav_items:
                text = await item.inner_text()
                if "deviation" in text.lower():
                    log_step("Navigation", f"Found Deviation link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/04_deviation_management.png", full_page=True)
                    
                    # Capture page content
                    content = await page.content()
                    with open(f"{output_dir}/deviation_management.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            # Explore CAPA
            log_step("Navigation", "Exploring CAPA")
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            for item in nav_items:
                text = await item.inner_text()
                if "capa" in text.lower():
                    log_step("Navigation", f"Found CAPA link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/05_capa.png", full_page=True)
                    
                    content = await page.content()
                    with open(f"{output_dir}/capa.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            # Explore Product Complaints
            log_step("Navigation", "Exploring Product Complaints")
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            for item in nav_items:
                text = await item.inner_text()
                if "complaint" in text.lower():
                    log_step("Navigation", f"Found Complaints link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/06_product_complaints.png", full_page=True)
                    
                    content = await page.content()
                    with open(f"{output_dir}/product_complaints.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            # Explore Recall Management
            log_step("Navigation", "Exploring Recall Management")
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            for item in nav_items:
                text = await item.inner_text()
                if "recall" in text.lower():
                    log_step("Navigation", f"Found Recall link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/07_recall_management.png", full_page=True)
                    
                    content = await page.content()
                    with open(f"{output_dir}/recall_management.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            # Explore Adverse Event Reporting
            log_step("Navigation", "Exploring Adverse Event Reporting")
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            for item in nav_items:
                text = await item.inner_text()
                if "adverse" in text.lower() or "event" in text.lower():
                    log_step("Navigation", f"Found Adverse Event link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/08_adverse_events.png", full_page=True)
                    
                    content = await page.content()
                    with open(f"{output_dir}/adverse_events.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            # Explore Supplier Management
            log_step("Navigation", "Exploring Supplier Management")
            nav_items = await page.query_selector_all('nav a, [role="navigation"] a, .sidebar a, .menu a')
            for item in nav_items:
                text = await item.inner_text()
                if "supplier" in text.lower():
                    log_step("Navigation", f"Found Supplier link: {text}")
                    await item.click()
                    await page.wait_for_load_state("networkidle", timeout=10000)
                    await asyncio.sleep(2)
                    await page.screenshot(path=f"{output_dir}/09_supplier_management.png", full_page=True)
                    
                    content = await page.content()
                    with open(f"{output_dir}/supplier_management.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    break
            
            log_step("Complete", "Exploration finished successfully")
            
        except Exception as e:
            log_step("Error", str(e))
            await page.screenshot(path=f"{output_dir}/error_screenshot.png", full_page=True)
        
        finally:
            # Save exploration log
            with open(f"{output_dir}/exploration_log.json", "w") as f:
                json.dump(exploration_log, f, indent=2)
            
            print("\n=== Exploration Complete ===")
            print(f"Screenshots and HTML saved to: {output_dir}/")
            print("Press Enter to close browser...")
            input()
            
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
