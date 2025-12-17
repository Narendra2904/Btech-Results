export async function fetchResult(htno: string) {
    const res = await fetch(
      `http://127.0.0.1:8000/result/${htno}`,
      { cache: "no-store" }
    );
  
    if (!res.ok) {
      throw new Error("Server error");
    }
  
    return res.json();
  }
  