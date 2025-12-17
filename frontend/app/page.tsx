"use client";

import { useState } from "react";
import Header from "@/components/Header";
import ResultCard from "@/components/ResultCard";
import Loader from "@/components/Loader";
import { fetchResult } from "@/lib/api";

export default function Home() {
  const [htno, setHtno] = useState("");
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const getResult = async () => {
    if (!htno) return alert("Hall Ticket enter chey ra 😅");

    setLoading(true);
    setError("");
    setData(null);

    try {
      const res = await fetchResult(htno);
      if (res.message) setError(res.message);
      else setData(res);
    } catch {
      setError("Server error 🥲");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen px-4">
      <Header />

      <div className="max-w-md mx-auto mt-10">
        <input
          className="w-full p-3 rounded bg-slate-800 text-white outline-none"
          placeholder="Enter Hall Ticket Number"
          value={htno}
          onChange={(e) => setHtno(e.target.value.toUpperCase())}
        />

        <button
          onClick={getResult}
          className="w-full mt-4 bg-sky-500 hover:bg-sky-600 p-3 rounded font-bold"
        >
          Get Result
        </button>

        {loading && <Loader />}
        {error && <p className="text-red-400 mt-4">{error}</p>}
        {data && <ResultCard data={data} />}
      </div>
    </main>
  );
}
