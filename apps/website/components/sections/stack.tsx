"use client"

import { motion } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { SectionParticles } from "@/components/canvas/section-particles"

const LAYERS = [
  {
    title: "Cognition Layer",
    body: "Memory, Knowledge Base, and Knowledge Graph work together to give the AI persistent intelligence. Memories are scored by relevance, accuracy, and impact. The Knowledge Base stores structured world knowledge as versioned entities on Arweave. The Knowledge Graph captures relationships between concepts, entities, and events — enabling second-order reasoning.",
  },
  {
    title: "Privacy Architecture",
    body: "User data is encrypted client-side with AES-256-GCM before it reaches the server. Encryption keys are derived deterministically from wallet signatures using HKDF-SHA256. Embeddings for private data use a local model that never sends data to external APIs. Two data scopes — user-scoped and shared cognition — are separated by architecture, not policy.",
  },
  {
    title: "Decentralized Infrastructure",
    body: "SIWE for authentication — no passwords, no emails, your wallet is your identity. IPFS for encrypted user data — mutable, portable, yours. Arweave for permanent world knowledge — censorship-resistant, permissionless. Lit Protocol for decentralized key management — no centralized custodian.",
  },
  {
    title: "Payments",
    body: "USDC on Payproof rails. Trustless, atomic, on-chain. Pay-as-you-go for compute — no payment processor, no subscription lock-in. Your wallet pays directly.",
  },
]

const TECH_BADGES = [
  "Claude", "FastAPI", "SIWE", "AES-256-GCM", "HKDF-SHA256",
  "IPFS", "Arweave", "Lit Protocol", "Voyage AI",
  "sentence-transformers", "USDC", "Payproof", "Next.js",
]

export function StackSection() {
  return (
    <SectionWrapper id="stack">
      <SectionParticles mode="drift" count={20} maxOpacity={0.1} />
      <SectionHeading number="05" title="THE STACK" />

      <div className="max-w-[720px] mx-auto px-2 sm:px-0">
        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="prose-body mb-16"
        >
          Built from first principles. Every layer serves trustlessness.
        </motion.p>

        <div className="space-y-12">
          {LAYERS.map((layer, i) => (
            <motion.div
              key={layer.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-40px" }}
              transition={{ duration: 0.6, delay: i * 0.1 }}
            >
              <h3 className="font-serif text-xl md:text-2xl text-foreground mb-4">
                {layer.title}
              </h3>
              <p className="prose-body">{layer.body}</p>
            </motion.div>
          ))}
        </div>

        {/* Tech badges */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="mt-16 flex flex-wrap gap-2 justify-center"
        >
          {TECH_BADGES.map((badge, i) => (
            <motion.span
              key={badge}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.3, delay: i * 0.04 }}
              className="font-mono text-[11px] tracking-wider uppercase px-3 py-1.5 rounded-full border border-accent/20 text-accent bg-accent/5"
            >
              {badge}
            </motion.span>
          ))}
        </motion.div>
      </div>
    </SectionWrapper>
  )
}
