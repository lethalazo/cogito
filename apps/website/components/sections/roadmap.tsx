"use client"

import { useRef } from "react"
import { motion, useScroll, useTransform } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { SectionParticles } from "@/components/canvas/section-particles"
import { cn } from "@/lib/utils"

const PHASES = [
  {
    date: "2026",
    title: "MVP — Trustless Cognitive AI",
    status: "active" as const,
    items: [
      "Working cognition layer — memory, knowledge base, knowledge graph",
      "SIWE wallet authentication — your wallet is your identity",
      "Client-side AES-256-GCM encryption — platform never sees plaintext",
      "IPFS user storage + Arweave shared cognition",
      "Dual embedding model — private local + public API",
      "Unified web interface",
    ],
  },
  {
    date: "2026–2027",
    title: "Specialist Agents",
    status: "upcoming" as const,
    items: [
      "Domain-specific cognitive agents — research, code, finance",
      "Agent switching in the unified interface",
      "Cross-agent shared cognition on Arweave",
      "Agent-to-agent invocation",
    ],
  },
  {
    date: "2027",
    title: "Deep Cognition",
    status: "upcoming" as const,
    items: [
      "World model — rich graph of entities, relationships, influence",
      "Second-order reasoning and cause-effect simulation",
      "Temporal reasoning — trends, cycles, time-dependent relationships",
    ],
  },
  {
    date: "2027+",
    title: "Self-Hosted Nodes",
    status: "upcoming" as const,
    items: [
      "Run your own Cogito node",
      "Cognitive portability — export and import your cognition",
      "TEE-based inference for privacy",
      "P2P node discovery and communication",
      "USDC micropayments for compute via Payproof",
    ],
  },
]

export function RoadmapSection() {
  const timelineRef = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({
    target: timelineRef,
    offset: ["start 0.8", "end 0.6"],
  })
  const lineScaleY = useTransform(scrollYProgress, [0, 1], ["0%", "100%"])

  return (
    <SectionWrapper id="roadmap" muted>
      <SectionParticles mode="rise" count={15} maxOpacity={0.08} />
      <SectionHeading number="06" title="ROADMAP" />

      <div className="max-w-[720px] mx-auto px-2 sm:px-0">
        <div ref={timelineRef} className="relative">
          <div className="absolute left-[7px] top-2 bottom-2 w-px bg-border/60" />
          <motion.div
            className="absolute left-[7px] top-2 w-px bg-accent/50 origin-top"
            style={{ height: lineScaleY }}
          />

          <div className="space-y-12">
            {PHASES.map((phase, i) => (
              <motion.div
                key={phase.date}
                initial={{ opacity: 0, x: -15 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true, margin: "-40px" }}
                transition={{ duration: 0.6, delay: i * 0.1 }}
                className="relative pl-8"
              >
                <div
                  className={cn(
                    "absolute left-0 top-1.5 w-[15px] h-[15px] rounded-full border-2 transition-all duration-500",
                    phase.status === "active" &&
                      "bg-accent border-accent animate-pulse-dot shadow-[0_0_15px_rgba(212,99,94,0.4)]",
                    phase.status === "upcoming" &&
                      "bg-background border-border"
                  )}
                />

                <span className="font-mono text-xs tracking-wider text-accent/70">
                  {phase.date}
                </span>
                <h3 className="font-serif text-xl md:text-2xl text-foreground mt-1 mb-4">
                  {phase.title}
                </h3>
                <ul className="space-y-2">
                  {phase.items.map((item, j) => (
                    <motion.li
                      key={item}
                      initial={{ opacity: 0, x: -8 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.4, delay: i * 0.1 + j * 0.05 }}
                      className="text-sm text-muted-foreground leading-relaxed pl-4 relative before:content-['–'] before:absolute before:left-0 before:text-accent-dim/40"
                    >
                      {item}
                    </motion.li>
                  ))}
                </ul>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </SectionWrapper>
  )
}
