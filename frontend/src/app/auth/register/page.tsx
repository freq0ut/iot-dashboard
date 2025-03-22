"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import axios from "@/lib/axios";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

export default function RegisterPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async () => {
    setError("");
    try {
      await axios.post("/users/register", { email, password });
      router.push("/auth/login");
    } catch (err: any) {
      setError(err?.response?.data?.detail || "Registration failed");
    }
  };

  return (
    <div className="max-w-sm mx-auto py-20">
      <h1 className="text-2xl font-bold mb-6">Register</h1>
      <Label>Email</Label>
      <Input value={email} onChange={(e) => setEmail(e.target.value)} type="email" />
      <Label className="mt-4">Password</Label>
      <Input value={password} onChange={(e) => setPassword(e.target.value)} type="password" />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      <Button className="mt-6 w-full" onClick={handleRegister}>Register</Button>
    </div>
  );
}
