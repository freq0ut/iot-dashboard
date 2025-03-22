"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import axios from "@/lib/axios";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    setError("");
    try {
      const res = await axios.post("/users/login", new URLSearchParams({
        username: email,
        password
      }), {
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
      });

      const token = res.data.access_token;
      localStorage.setItem("token", token);
      router.push("/dashboard");
    } catch (err: any) {
      setError(err?.response?.data?.detail || "Login failed");
    }
  };

  return (
    <div className="max-w-sm mx-auto py-20">
      <h1 className="text-2xl font-bold mb-6">Login</h1>
      <Label>Email</Label>
      <Input value={email} onChange={(e) => setEmail(e.target.value)} type="email" />
      <Label className="mt-4">Password</Label>
      <Input value={password} onChange={(e) => setPassword(e.target.value)} type="password" />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      <Button className="mt-6 w-full" onClick={handleLogin}>Login</Button>
    </div>
  );
}
